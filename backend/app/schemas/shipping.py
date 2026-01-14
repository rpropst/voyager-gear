"""Pydantic schemas for shipping and tax calculations."""
from pydantic import BaseModel, Field


class ShippingTaxRequest(BaseModel):
    """Schema for shipping and tax calculation request."""

    zip_code: str = Field(..., min_length=5, max_length=10, description="ZIP code for calculation")
    subtotal: float = Field(..., gt=0, description="Cart subtotal")


class ShippingTaxResponse(BaseModel):
    """Schema for shipping and tax calculation response."""

    zip_code: str
    state: str
    tax_rate: float
    shipping_cost: float
    subtotal: float
    tax_amount: float
    shipping_amount: float
    total: float

    class Config:
        from_attributes = True
