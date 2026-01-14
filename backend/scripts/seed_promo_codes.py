"""Seed script to populate the database with sample promo codes."""
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add parent directory to path to import app modules
sys.path.append(str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session

from app.database import SessionLocal, init_db
from app.models.promo_code import PromoCode


def seed_promo_codes(db: Session):
    """Seed the database with sample promo codes."""

    # Check if promo codes already exist
    existing_count = db.query(PromoCode).count()
    if existing_count > 0:
        print(f"Database already contains {existing_count} promo codes. Skipping seed.")
        return

    # Calculate expiration dates
    one_month = datetime.utcnow() + timedelta(days=30)
    three_months = datetime.utcnow() + timedelta(days=90)
    six_months = datetime.utcnow() + timedelta(days=180)

    promo_codes = [
        PromoCode(
            code="WELCOME10",
            discount_percentage=10.0,
            is_active=True,
            usage_limit=None,  # Unlimited
            times_used=0,
            expires_at=None,  # No expiration
        ),
        PromoCode(
            code="SAVE20",
            discount_percentage=20.0,
            is_active=True,
            usage_limit=None,  # Unlimited
            times_used=0,
            expires_at=None,  # No expiration
        ),
        PromoCode(
            code="SUMMER15",
            discount_percentage=15.0,
            is_active=True,
            usage_limit=100,  # Limited to 100 uses
            times_used=0,
            expires_at=six_months,  # Expires in 6 months
        ),
        PromoCode(
            code="NEWYEAR25",
            discount_percentage=25.0,
            is_active=True,
            usage_limit=50,  # Limited to 50 uses
            times_used=0,
            expires_at=one_month,  # Expires in 1 month
        ),
        PromoCode(
            code="TRAVEL5",
            discount_percentage=5.0,
            is_active=True,
            usage_limit=None,  # Unlimited
            times_used=0,
            expires_at=None,  # No expiration
        ),
        PromoCode(
            code="BIGTRIP30",
            discount_percentage=30.0,
            is_active=True,
            usage_limit=25,  # Limited to 25 uses
            times_used=0,
            expires_at=three_months,  # Expires in 3 months
        ),
        PromoCode(
            code="FREESHIP",
            discount_percentage=10.0,
            is_active=True,
            usage_limit=200,  # Limited to 200 uses
            times_used=0,
            expires_at=six_months,  # Expires in 6 months
        ),
        PromoCode(
            code="EXPIRED",
            discount_percentage=50.0,
            is_active=True,
            usage_limit=None,
            times_used=0,
            expires_at=datetime.utcnow() - timedelta(days=1),  # Already expired (for testing)
        ),
        PromoCode(
            code="INACTIVE",
            discount_percentage=40.0,
            is_active=False,  # Inactive (for testing)
            usage_limit=None,
            times_used=0,
            expires_at=None,
        ),
    ]

    # Add all promo codes to database
    db.add_all(promo_codes)
    db.commit()

    print(f"Successfully seeded {len(promo_codes)} promo codes!")
    print("\nActive promo codes:")
    for code in promo_codes:
        if code.is_active and (not code.expires_at or code.expires_at > datetime.utcnow()):
            status = f"{code.discount_percentage}% off"
            if code.usage_limit:
                status += f" (limit: {code.usage_limit})"
            if code.expires_at:
                days_left = (code.expires_at - datetime.utcnow()).days
                status += f" (expires in {days_left} days)"
            else:
                status += " (no expiration)"
            print(f"  - {code.code}: {status}")


def main():
    """Main function to run the seed script."""
    print("Initializing database...")
    init_db()

    print("Starting promo code seed...")
    db = SessionLocal()
    try:
        seed_promo_codes(db)
    except Exception as e:
        print(f"Error seeding promo codes: {e}")
        db.rollback()
    finally:
        db.close()

    print("\nSeed complete!")


if __name__ == "__main__":
    main()
