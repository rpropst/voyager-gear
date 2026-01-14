"""
SavedItem Model
Represents an item saved for later in a user's cart
"""

from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base


class SavedItem(Base):
    """
    Saved item model - represents a product saved for later with quantity
    """
    __tablename__ = "saved_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    cart = relationship("Cart", back_populates="saved_items")
    product = relationship("Product")

    # Unique constraint: one product can only appear once in saved items per cart
    __table_args__ = (
        UniqueConstraint('cart_id', 'product_id', name='uix_saved_cart_product'),
    )

    def __repr__(self):
        return f"<SavedItem(id={self.id}, cart_id={self.cart_id}, product_id={self.product_id}, quantity={self.quantity})>"
