"""
PromoCode Model
Represents a promotional discount code
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from app.database import Base


class PromoCode(Base):
    """
    Promo code model - represents a discount code with validation rules
    """
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    discount_percentage = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    usage_limit = Column(Integer, nullable=True)  # NULL = unlimited
    times_used = Column(Integer, default=0, nullable=False)
    expires_at = Column(DateTime, nullable=True)  # NULL = no expiration
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def is_valid(self) -> bool:
        """Check if promo code is currently valid"""
        # Check if active
        if not self.is_active:
            return False

        # Check expiration
        if self.expires_at and datetime.utcnow() > self.expires_at:
            return False

        # Check usage limit
        if self.usage_limit is not None and self.times_used >= self.usage_limit:
            return False

        return True

    def __repr__(self):
        return f"<PromoCode(id={self.id}, code={self.code}, discount={self.discount_percentage}%)>"
