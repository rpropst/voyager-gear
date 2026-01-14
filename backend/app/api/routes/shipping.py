"""Shipping and tax calculation API routes."""
from fastapi import APIRouter, HTTPException, status

from app.core.rates import calculate_shipping_and_tax
from app.schemas.shipping import ShippingTaxRequest, ShippingTaxResponse

router = APIRouter(prefix="/shipping", tags=["shipping"])


@router.post("/calculate", response_model=ShippingTaxResponse)
def calculate_shipping_tax(request_data: ShippingTaxRequest):
    """
    Calculate shipping and tax based on ZIP code and subtotal.

    Args:
        request_data: ZIP code and cart subtotal

    Returns:
        Shipping and tax calculation breakdown

    Raises:
        HTTPException: If ZIP code is invalid
    """
    try:
        state, tax_rate, shipping_cost, tax_amount, shipping_amount, total = calculate_shipping_and_tax(
            request_data.zip_code,
            request_data.subtotal
        )

        return ShippingTaxResponse(
            zip_code=request_data.zip_code,
            state=state,
            tax_rate=tax_rate,
            shipping_cost=shipping_cost,
            subtotal=request_data.subtotal,
            tax_amount=tax_amount,
            shipping_amount=shipping_amount,
            total=total
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
