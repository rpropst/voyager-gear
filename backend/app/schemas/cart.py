"""Pydantic schemas for Cart models."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.product import ProductResponse


class CartItemBase(BaseModel):
    """Base cart item schema."""

    product_id: int = Field(..., gt=0, description="Product ID")
    quantity: int = Field(..., gt=0, description="Item quantity")


class CartItemCreate(CartItemBase):
    """Schema for adding an item to cart."""

    pass


class CartItemUpdate(BaseModel):
    """Schema for updating a cart item."""

    quantity: int = Field(..., gt=0, description="Updated quantity")


class CartItemResponse(CartItemBase):
    """Schema for cart item response."""

    id: int
    cart_id: int
    product: ProductResponse
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SavedItemResponse(BaseModel):
    """Schema for saved item response."""

    id: int
    cart_id: int
    product_id: int
    quantity: int
    product: ProductResponse
    created_at: datetime

    class Config:
        from_attributes = True


class CartResponse(BaseModel):
    """Schema for cart response."""

    id: int
    user_id: int
    items: list[CartItemResponse]
    saved_items: list[SavedItemResponse]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class GuestCartItem(BaseModel):
    """Schema for guest cart item (from localStorage)."""

    product_id: int = Field(..., gt=0, description="Product ID")
    quantity: int = Field(..., gt=0, description="Item quantity")


class GuestCartMerge(BaseModel):
    """Schema for merging guest cart with user cart."""

    items: list[GuestCartItem] = Field(..., description="Guest cart items to merge")
