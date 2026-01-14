"""Pydantic schemas for PromoCode model."""
from pydantic import BaseModel, Field


class PromoCodeValidate(BaseModel):
    """Schema for validating a promo code."""

    code: str = Field(..., min_length=1, max_length=50, description="Promo code to validate")


class PromoCodeResponse(BaseModel):
    """Schema for promo code validation response."""

    code: str
    discount_percentage: float
    is_valid: bool
    message: str | None = None

    class Config:
        from_attributes = True
