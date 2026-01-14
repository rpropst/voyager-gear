"""Cart API routes."""
from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session, joinedload

from app.api.deps import get_current_user
from app.core.exceptions import OutOfStockError, CartNotFoundError
from app.database import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.saved_item import SavedItem
from app.models.product import Product
from app.models.user import User
from app.schemas.cart import (
    CartItemCreate,
    CartItemUpdate,
    CartResponse,
    GuestCartMerge,
)

router = APIRouter(prefix="/cart", tags=["cart"])


def get_or_create_cart(db: Session, user: User) -> Cart:
    """
    Get user's cart or create one if it doesn't exist.

    Args:
        db: Database session
        user: Current user

    Returns:
        User's cart
    """
    cart = db.query(Cart).filter(Cart.user_id == user.id).first()

    if not cart:
        cart = Cart(user_id=user.id)
        db.add(cart)
        db.commit()
        db.refresh(cart)

    return cart


@router.get("", response_model=CartResponse)
def get_cart(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Get current user's cart with all items.

    Args:
        current_user: Authenticated user
        db: Database session

    Returns:
        User's cart with items and saved items
    """
    cart = get_or_create_cart(db, current_user)

    # Eagerly load relationships
    cart = db.query(Cart)\
        .filter(Cart.id == cart.id)\
        .options(
            joinedload(Cart.items).joinedload(CartItem.product),
            joinedload(Cart.saved_items).joinedload(SavedItem.product)
        )\
        .first()

    return cart


@router.post("/items", response_model=CartResponse, status_code=status.HTTP_201_CREATED)
def add_to_cart(
    item_data: CartItemCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Add an item to cart or increment quantity if it already exists.

    Args:
        item_data: Item to add (product_id and quantity)
        current_user: Authenticated user
        db: Database session

    Returns:
        Updated cart

    Raises:
        OutOfStockError: If requested quantity exceeds available stock
    """
    # Get or create cart
    cart = get_or_create_cart(db, current_user)

    # Check if product exists and has sufficient stock
    product = db.query(Product).filter(Product.id == item_data.product_id).first()
    if not product:
        raise OutOfStockError("Product not found")

    # Check if item already exists in cart
    existing_item = db.query(CartItem)\
        .filter(CartItem.cart_id == cart.id, CartItem.product_id == item_data.product_id)\
        .first()

    if existing_item:
        # Increment quantity
        new_quantity = existing_item.quantity + item_data.quantity
        if new_quantity > product.stock:
            raise OutOfStockError(
                f"Only {product.stock} units available. You already have {existing_item.quantity} in your cart."
            )
        existing_item.quantity = new_quantity
    else:
        # Check stock availability
        if item_data.quantity > product.stock:
            raise OutOfStockError(f"Only {product.stock} units available")

        # Create new cart item
        new_item = CartItem(
            cart_id=cart.id,
            product_id=item_data.product_id,
            quantity=item_data.quantity
        )
        db.add(new_item)

    db.commit()

    # Return updated cart with eager loading
    cart = db.query(Cart)\
        .filter(Cart.id == cart.id)\
        .options(
            joinedload(Cart.items).joinedload(CartItem.product),
            joinedload(Cart.saved_items).joinedload(SavedItem.product)
        )\
        .first()

    return cart


@router.put("/items/{item_id}", response_model=CartResponse)
def update_cart_item(
    item_id: int,
    item_data: CartItemUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Update cart item quantity.

    Args:
        item_id: Cart item ID
        item_data: Updated quantity
        current_user: Authenticated user
        db: Database session

    Returns:
        Updated cart

    Raises:
        OutOfStockError: If requested quantity exceeds available stock
        CartNotFoundError: If cart item not found
    """
    # Get user's cart
    cart = get_or_create_cart(db, current_user)

    # Find cart item
    cart_item = db.query(CartItem)\
        .filter(CartItem.id == item_id, CartItem.cart_id == cart.id)\
        .first()

    if not cart_item:
        raise CartNotFoundError("Cart item not found")

    # Check stock availability
    product = db.query(Product).filter(Product.id == cart_item.product_id).first()
    if item_data.quantity > product.stock:
        raise OutOfStockError(f"Only {product.stock} units available")

    # Update quantity
    cart_item.quantity = item_data.quantity
    db.commit()

    # Return updated cart
    cart = db.query(Cart)\
        .filter(Cart.id == cart.id)\
        .options(
            joinedload(Cart.items).joinedload(CartItem.product),
            joinedload(Cart.saved_items).joinedload(SavedItem.product)
        )\
        .first()

    return cart


@router.delete("/items/{item_id}", response_model=CartResponse)
def remove_cart_item(
    item_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Remove an item from cart.

    Args:
        item_id: Cart item ID
        current_user: Authenticated user
        db: Database session

    Returns:
        Updated cart

    Raises:
        CartNotFoundError: If cart item not found
    """
    # Get user's cart
    cart = get_or_create_cart(db, current_user)

    # Find and delete cart item
    cart_item = db.query(CartItem)\
        .filter(CartItem.id == item_id, CartItem.cart_id == cart.id)\
        .first()

    if not cart_item:
        raise CartNotFoundError("Cart item not found")

    db.delete(cart_item)
    db.commit()

    # Return updated cart
    cart = db.query(Cart)\
        .filter(Cart.id == cart.id)\
        .options(
            joinedload(Cart.items).joinedload(CartItem.product),
            joinedload(Cart.saved_items).joinedload(SavedItem.product)
        )\
        .first()

    return cart


@router.post("/merge", response_model=CartResponse)
def merge_guest_cart(
    guest_cart_data: GuestCartMerge,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Merge guest cart with user's cart on login.
    Combines quantities for duplicate products.

    Args:
        guest_cart_data: Guest cart items from localStorage
        current_user: Authenticated user
        db: Database session

    Returns:
        Merged cart

    Raises:
        OutOfStockError: If merged quantity exceeds available stock
    """
    # Get or create cart
    cart = get_or_create_cart(db, current_user)

    # Merge each guest cart item
    for guest_item in guest_cart_data.items:
        # Check if product exists and has sufficient stock
        product = db.query(Product).filter(Product.id == guest_item.product_id).first()
        if not product:
            continue  # Skip invalid products

        # Check if item already exists in cart
        existing_item = db.query(CartItem)\
            .filter(CartItem.cart_id == cart.id, CartItem.product_id == guest_item.product_id)\
            .first()

        if existing_item:
            # Combine quantities
            new_quantity = existing_item.quantity + guest_item.quantity
            if new_quantity > product.stock:
                # Cap at available stock
                existing_item.quantity = product.stock
            else:
                existing_item.quantity = new_quantity
        else:
            # Add new item
            if guest_item.quantity > product.stock:
                # Cap at available stock
                quantity = product.stock
            else:
                quantity = guest_item.quantity

            new_item = CartItem(
                cart_id=cart.id,
                product_id=guest_item.product_id,
                quantity=quantity
            )
            db.add(new_item)

    db.commit()

    # Return merged cart
    cart = db.query(Cart)\
        .filter(Cart.id == cart.id)\
        .options(
            joinedload(Cart.items).joinedload(CartItem.product),
            joinedload(Cart.saved_items).joinedload(SavedItem.product)
        )\
        .first()

    return cart


@router.post("/items/{item_id}/save", response_model=CartResponse)
def save_for_later(
    item_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Move cart item to saved for later.

    Args:
        item_id: Cart item ID
        current_user: Authenticated user
        db: Database session

    Returns:
        Updated cart

    Raises:
        CartNotFoundError: If cart item not found
    """
    # Get user's cart
    cart = get_or_create_cart(db, current_user)

    # Find cart item
    cart_item = db.query(CartItem)\
        .filter(CartItem.id == item_id, CartItem.cart_id == cart.id)\
        .first()

    if not cart_item:
        raise CartNotFoundError("Cart item not found")

    # Check if already saved
    existing_saved = db.query(SavedItem)\
        .filter(SavedItem.cart_id == cart.id, SavedItem.product_id == cart_item.product_id)\
        .first()

    if existing_saved:
        # Update quantity
        existing_saved.quantity = cart_item.quantity
    else:
        # Create saved item
        saved_item = SavedItem(
            cart_id=cart.id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity
        )
        db.add(saved_item)

    # Remove from cart
    db.delete(cart_item)
    db.commit()

    # Return updated cart
    cart = db.query(Cart)\
        .filter(Cart.id == cart.id)\
        .options(
            joinedload(Cart.items).joinedload(CartItem.product),
            joinedload(Cart.saved_items).joinedload(SavedItem.product)
        )\
        .first()

    return cart


@router.post("/saved/{saved_id}/restore", response_model=CartResponse)
def restore_saved_item(
    saved_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Restore saved item back to cart.

    Args:
        saved_id: Saved item ID
        current_user: Authenticated user
        db: Database session

    Returns:
        Updated cart

    Raises:
        CartNotFoundError: If saved item not found
        OutOfStockError: If product is out of stock
    """
    # Get user's cart
    cart = get_or_create_cart(db, current_user)

    # Find saved item
    saved_item = db.query(SavedItem)\
        .filter(SavedItem.id == saved_id, SavedItem.cart_id == cart.id)\
        .first()

    if not saved_item:
        raise CartNotFoundError("Saved item not found")

    # Check stock availability
    product = db.query(Product).filter(Product.id == saved_item.product_id).first()
    if saved_item.quantity > product.stock:
        raise OutOfStockError(f"Only {product.stock} units available")

    # Check if already in cart
    existing_item = db.query(CartItem)\
        .filter(CartItem.cart_id == cart.id, CartItem.product_id == saved_item.product_id)\
        .first()

    if existing_item:
        # Add to existing quantity
        new_quantity = existing_item.quantity + saved_item.quantity
        if new_quantity > product.stock:
            raise OutOfStockError(f"Only {product.stock} units available")
        existing_item.quantity = new_quantity
    else:
        # Create cart item
        cart_item = CartItem(
            cart_id=cart.id,
            product_id=saved_item.product_id,
            quantity=saved_item.quantity
        )
        db.add(cart_item)

    # Remove from saved
    db.delete(saved_item)
    db.commit()

    # Return updated cart
    cart = db.query(Cart)\
        .filter(Cart.id == cart.id)\
        .options(
            joinedload(Cart.items).joinedload(CartItem.product),
            joinedload(Cart.saved_items).joinedload(SavedItem.product)
        )\
        .first()

    return cart


@router.delete("/saved/{saved_id}", response_model=CartResponse)
def remove_saved_item(
    saved_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Delete a saved item.

    Args:
        saved_id: Saved item ID
        current_user: Authenticated user
        db: Database session

    Returns:
        Updated cart

    Raises:
        CartNotFoundError: If saved item not found
    """
    # Get user's cart
    cart = get_or_create_cart(db, current_user)

    # Find and delete saved item
    saved_item = db.query(SavedItem)\
        .filter(SavedItem.id == saved_id, SavedItem.cart_id == cart.id)\
        .first()

    if not saved_item:
        raise CartNotFoundError("Saved item not found")

    db.delete(saved_item)
    db.commit()

    # Return updated cart
    cart = db.query(Cart)\
        .filter(Cart.id == cart.id)\
        .options(
            joinedload(Cart.items).joinedload(CartItem.product),
            joinedload(Cart.saved_items).joinedload(SavedItem.product)
        )\
        .first()

    return cart


@router.post("/clear", status_code=status.HTTP_204_NO_CONTENT)
def clear_cart(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    """
    Clear all items from cart.

    Args:
        current_user: Authenticated user
        db: Database session
    """
    # Get user's cart
    cart = get_or_create_cart(db, current_user)

    # Delete all cart items
    db.query(CartItem).filter(CartItem.cart_id == cart.id).delete()
    db.commit()

    return None
