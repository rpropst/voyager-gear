"""Promo code API routes."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.exceptions import InvalidPromoCodeError
from app.database import get_db
from app.models.promo_code import PromoCode
from app.schemas.promo_code import PromoCodeValidate, PromoCodeResponse

router = APIRouter(prefix="/promo-codes", tags=["promo codes"])


@router.post("/validate", response_model=PromoCodeResponse)
def validate_promo_code(
    code_data: PromoCodeValidate,
    db: Session = Depends(get_db)
):
    """
    Validate a promo code.

    Args:
        code_data: Promo code to validate
        db: Database session

    Returns:
        Promo code validation result

    Raises:
        InvalidPromoCodeError: If code is invalid, expired, or exceeded usage limit
    """
    # Find promo code (case-insensitive)
    promo_code = db.query(PromoCode)\
        .filter(PromoCode.code.ilike(code_data.code))\
        .first()

    if not promo_code:
        return PromoCodeResponse(
            code=code_data.code,
            discount_percentage=0.0,
            is_valid=False,
            message="Invalid promo code"
        )

    # Check if valid using model method
    if not promo_code.is_valid():
        # Determine specific reason
        if not promo_code.is_active:
            message = "This promo code is no longer active"
        elif promo_code.expires_at and promo_code.expires_at < promo_code.expires_at.__class__.utcnow():
            message = "This promo code has expired"
        elif promo_code.usage_limit is not None and promo_code.times_used >= promo_code.usage_limit:
            message = "This promo code has reached its usage limit"
        else:
            message = "Invalid promo code"

        return PromoCodeResponse(
            code=promo_code.code,
            discount_percentage=promo_code.discount_percentage,
            is_valid=False,
            message=message
        )

    # Valid code
    return PromoCodeResponse(
        code=promo_code.code,
        discount_percentage=promo_code.discount_percentage,
        is_valid=True,
        message=f"Promo code applied! You save {promo_code.discount_percentage}%"
    )
