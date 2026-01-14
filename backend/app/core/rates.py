"""
Tax and shipping rate utilities
Provides lookup tables and functions for calculating tax and shipping costs
"""

from typing import Tuple

# State tax rates (simplified average rates for each state)
STATE_TAX_RATES = {
    "AL": 0.0400,  # Alabama
    "AK": 0.0000,  # Alaska (no state sales tax)
    "AZ": 0.0560,  # Arizona
    "AR": 0.0650,  # Arkansas
    "CA": 0.0725,  # California
    "CO": 0.0290,  # Colorado
    "CT": 0.0635,  # Connecticut
    "DE": 0.0000,  # Delaware (no sales tax)
    "FL": 0.0600,  # Florida
    "GA": 0.0400,  # Georgia
    "HI": 0.0400,  # Hawaii
    "ID": 0.0600,  # Idaho
    "IL": 0.0625,  # Illinois
    "IN": 0.0700,  # Indiana
    "IA": 0.0600,  # Iowa
    "KS": 0.0650,  # Kansas
    "KY": 0.0600,  # Kentucky
    "LA": 0.0445,  # Louisiana
    "ME": 0.0550,  # Maine
    "MD": 0.0600,  # Maryland
    "MA": 0.0625,  # Massachusetts
    "MI": 0.0600,  # Michigan
    "MN": 0.0688,  # Minnesota
    "MS": 0.0700,  # Mississippi
    "MO": 0.0423,  # Missouri
    "MT": 0.0000,  # Montana (no sales tax)
    "NE": 0.0550,  # Nebraska
    "NV": 0.0685,  # Nevada
    "NH": 0.0000,  # New Hampshire (no sales tax)
    "NJ": 0.0663,  # New Jersey
    "NM": 0.0513,  # New Mexico
    "NY": 0.0400,  # New York
    "NC": 0.0475,  # North Carolina
    "ND": 0.0500,  # North Dakota
    "OH": 0.0575,  # Ohio
    "OK": 0.0450,  # Oklahoma
    "OR": 0.0000,  # Oregon (no sales tax)
    "PA": 0.0600,  # Pennsylvania
    "RI": 0.0700,  # Rhode Island
    "SC": 0.0600,  # South Carolina
    "SD": 0.0450,  # South Dakota
    "TN": 0.0700,  # Tennessee
    "TX": 0.0625,  # Texas
    "UT": 0.0610,  # Utah
    "VT": 0.0600,  # Vermont
    "VA": 0.0530,  # Virginia
    "WA": 0.0650,  # Washington
    "WV": 0.0600,  # West Virginia
    "WI": 0.0500,  # Wisconsin
    "WY": 0.0400,  # Wyoming
    "DC": 0.0600,  # District of Columbia
}

# ZIP code prefix to state mapping (first 3 digits of ZIP code)
# Format: (min_prefix, max_prefix): state_code
ZIP_PREFIX_TO_STATE = {
    # Alabama
    (350, 369): "AL",
    # Alaska
    (995, 999): "AK",
    # Arizona
    (850, 865): "AZ",
    # Arkansas
    (716, 729): "AR",
    # California
    (900, 961): "CA",
    # Colorado
    (800, 816): "CO",
    # Connecticut
    (60, 69): "CT",
    # Delaware
    (197, 199): "DE",
    # Florida
    (320, 349): "FL",
    # Georgia
    (300, 319): "GA",
    (398, 399): "GA",
    # Hawaii
    (967, 968): "HI",
    # Idaho
    (832, 838): "ID",
    # Illinois
    (600, 629): "IL",
    # Indiana
    (460, 479): "IN",
    # Iowa
    (500, 528): "IA",
    # Kansas
    (660, 679): "KS",
    # Kentucky
    (400, 427): "KY",
    # Louisiana
    (700, 714): "LA",
    # Maine
    (39, 49): "ME",
    # Maryland
    (206, 219): "MD",
    # Massachusetts
    (10, 27): "MA",
    # Michigan
    (480, 499): "MI",
    # Minnesota
    (550, 567): "MN",
    # Mississippi
    (386, 397): "MS",
    # Missouri
    (630, 658): "MO",
    # Montana
    (590, 599): "MT",
    # Nebraska
    (680, 693): "NE",
    # Nevada
    (889, 898): "NV",
    # New Hampshire
    (30, 38): "NH",
    # New Jersey
    (70, 89): "NJ",
    # New Mexico
    (870, 884): "NM",
    # New York
    (100, 149): "NY",
    # North Carolina
    (270, 289): "NC",
    # North Dakota
    (580, 588): "ND",
    # Ohio
    (430, 459): "OH",
    # Oklahoma
    (730, 749): "OK",
    # Oregon
    (970, 979): "OR",
    # Pennsylvania
    (150, 196): "PA",
    # Rhode Island
    (28, 29): "RI",
    # South Carolina
    (290, 299): "SC",
    # South Dakota
    (570, 577): "SD",
    # Tennessee
    (370, 385): "TN",
    # Texas
    (750, 799): "TX",
    (885, 885): "TX",
    # Utah
    (840, 847): "UT",
    # Vermont
    (50, 59): "VT",
    # Virginia
    (220, 246): "VA",
    # Washington
    (980, 994): "WA",
    # West Virginia
    (247, 268): "WV",
    # Wisconsin
    (530, 549): "WI",
    # Wyoming
    (820, 831): "WY",
    # DC
    (200, 205): "DC",
}


def get_state_from_zip(zip_code: str) -> str:
    """
    Get state code from ZIP code.

    Args:
        zip_code: 5-digit ZIP code (can include dash and extra digits)

    Returns:
        State code (e.g., "CA", "NY") or "UNKNOWN"

    Raises:
        ValueError: If ZIP code is invalid format
    """
    # Remove any non-numeric characters and get first 5 digits
    clean_zip = ''.join(c for c in zip_code if c.isdigit())

    if len(clean_zip) < 5:
        raise ValueError("ZIP code must be at least 5 digits")

    # Get first 3 digits as prefix
    prefix = int(clean_zip[:3])

    # Look up state
    for (min_prefix, max_prefix), state in ZIP_PREFIX_TO_STATE.items():
        if min_prefix <= prefix <= max_prefix:
            return state

    return "UNKNOWN"


def get_tax_rate(state: str) -> float:
    """
    Get tax rate for a state.

    Args:
        state: State code (e.g., "CA", "NY")

    Returns:
        Tax rate as decimal (e.g., 0.0725 for 7.25%)
    """
    return STATE_TAX_RATES.get(state.upper(), 0.0)


def calculate_shipping_cost(subtotal: float) -> float:
    """
    Calculate shipping cost based on subtotal.

    Tiered shipping rates:
    - $50 or more: FREE
    - $25 to $49.99: $5.99
    - Under $25: $9.99

    Args:
        subtotal: Cart subtotal before tax and shipping

    Returns:
        Shipping cost
    """
    if subtotal >= 50.0:
        return 0.0
    elif subtotal >= 25.0:
        return 5.99
    else:
        return 9.99


def calculate_shipping_and_tax(zip_code: str, subtotal: float) -> Tuple[str, float, float, float, float, float]:
    """
    Calculate complete shipping and tax information.

    Args:
        zip_code: Customer's ZIP code
        subtotal: Cart subtotal before tax and shipping

    Returns:
        Tuple of (state, tax_rate, shipping_cost, tax_amount, shipping_amount, total)

    Raises:
        ValueError: If ZIP code is invalid
    """
    state = get_state_from_zip(zip_code)

    if state == "UNKNOWN":
        raise ValueError("Invalid ZIP code")

    tax_rate = get_tax_rate(state)
    shipping_cost = calculate_shipping_cost(subtotal)

    tax_amount = subtotal * tax_rate
    shipping_amount = shipping_cost
    total = subtotal + tax_amount + shipping_amount

    return state, tax_rate, shipping_cost, tax_amount, shipping_amount, total
