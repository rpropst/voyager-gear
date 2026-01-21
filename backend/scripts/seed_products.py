"""Seed script to populate the database with sample products."""
import sys
from pathlib import Path

# Add parent directory to path to import app modules
sys.path.append(str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session

from app.database import SessionLocal, init_db
from app.models.product import Product, ProductCategory


def seed_products(db: Session):
    """Seed the database with sample products."""

    # Clear existing products for fresh seed
    existing_count = db.query(Product).count()
    if existing_count > 0:
        print(f"Clearing {existing_count} existing products...")
        db.query(Product).delete()
        db.commit()

    products = [
        # LUGGAGE - 30 items
        Product(
            name="Rolling Hardside Spinner Large",
            description="Durable hardside luggage with 360° spinner wheels. TSA-approved lock, expandable design, and scratch-resistant finish. Perfect for long trips.",
            price=249.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1565026057447-bc90a3dceb87?w=800",
            stock=25
        ),
        Product(
            name="Carry-On Hardshell Suitcase",
            description="Lightweight carry-on with polycarbonate shell. Fits in overhead compartments. Interior compression straps and zippered divider.",
            price=149.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1596969490001-f4e29c3e1a99?w=800",
            stock=40
        ),
        Product(
            name="Travel Duffel Bag Large",
            description="Water-resistant polyester duffel with adjustable shoulder strap. Multiple compartments including shoe pocket. Ideal for weekend getaways.",
            price=89.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=30
        ),
        Product(
            name="Vintage Leather Suitcase",
            description="Premium full-grain leather suitcase with brass hardware. Vintage-inspired design meets modern functionality. Lined interior with pockets.",
            price=399.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1596194292724-9ca8389e2af5?w=800",
            stock=15
        ),
        Product(
            name="Kids Rolling Backpack",
            description="Colorful rolling backpack for children. Telescopic handle, padded back straps for versatile carrying. Fun patterns and durable construction.",
            price=79.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1546938576-6e6a64f317cc?w=800",
            stock=20
        ),
        Product(
            name="Soft-Sided Expandable Luggage",
            description="Versatile soft-sided luggage with expandable capacity. Four multi-directional spinner wheels. Interior organization pockets.",
            price=179.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1585146777216-d05f72ce1ed5?w=800",
            stock=35
        ),
        Product(
            name="Aluminum Frame Suitcase Pro",
            description="Professional aluminum-frame suitcase with reinforced corners. Premium quality for frequent travelers. Lifetime warranty included.",
            price=449.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1591791068607-ee346a55d47e?w=800",
            stock=12
        ),
        Product(
            name="Garment Bag Travel Suit Carrier",
            description="Tri-fold garment bag for suits and dresses. Water-resistant nylon with multiple pockets. Keeps clothes wrinkle-free during travel.",
            price=69.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=18
        ),
        Product(
            name="Checked Luggage Extra Large",
            description="Extra-large checked luggage for extended trips. 32-inch height, expandable design adds 2 inches. Reinforced handle system.",
            price=199.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=800",
            stock=22
        ),
        Product(
            name="Underseat Carry-On Tote",
            description="Compact tote designed to fit under airplane seats. Multiple interior and exterior pockets. Perfect for essentials and electronics.",
            price=49.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1574662875393-2e4c0e44cc13?w=800",
            stock=45
        ),
        Product(
            name="Hybrid Spinner Luggage Set",
            description="3-piece luggage set with matching design. Includes carry-on, medium, and large sizes. Nested storage saves space at home.",
            price=399.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1590003124022-424c5a026422?w=800",
            stock=10
        ),
        Product(
            name="Wheeled Backpack Convertible",
            description="2-in-1 convertible backpack with detachable wheels. Laptop compartment and USB charging port. Airport security friendly.",
            price=129.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1581553680321-4aadc7c23b7a?w=800",
            stock=28
        ),
        Product(
            name="Travel Trunk Vintage Style",
            description="Steamer trunk inspired design with modern features. Perfect for cruise ships and vintage enthusiasts. Spacious interior with tray.",
            price=299.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1604482423767-1bf5d6a2e566?w=800",
            stock=8
        ),
        Product(
            name="Lightweight Carry-On Spinner",
            description="Ultra-lightweight carry-on weighing only 5.5 lbs. Maximizes your carry-on weight allowance. Durable construction despite low weight.",
            price=139.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1589975876563-18d8a87e8c7e?w=800",
            stock=32
        ),
        Product(
            name="Business Rolling Briefcase",
            description="Professional rolling briefcase with laptop compartment. Fits up to 17-inch laptop. Organized pockets for documents and accessories.",
            price=189.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1622560480605-d83c853bc5c3?w=800",
            stock=16
        ),
        # Additional LUGGAGE items
        Product(
            name="Compact Carry-On Spinner",
            description="Ultra-compact spinner designed for overhead bins. Hardshell polycarbonate construction with organized interior pockets.",
            price=159.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1565026057447-bc90a3dceb87?w=800",
            stock=29
        ),
        Product(
            name="Travel Backpack Suitcase Hybrid",
            description="Innovative hybrid between backpack and suitcase. Detachable daypack included. Perfect for adventure travelers.",
            price=219.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=18
        ),
        Product(
            name="Hard Case Luggage Set 2-Piece",
            description="Matching 2-piece hardcase set with mirror finish. Lightweight yet durable. Includes carry-on and checked sizes.",
            price=329.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1590003124022-424c5a026422?w=800",
            stock=14
        ),
        Product(
            name="Spinner Luggage with USB Port",
            description="Smart luggage with integrated USB charging port and power bank pocket. TSA-compliant design.",
            price=199.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1585146777216-d05f72ce1ed5?w=800",
            stock=26
        ),
        Product(
            name="Luxury Designer Carry-On",
            description="Premium designer carry-on with Italian leather accents. Hand-crafted details and lifetime warranty.",
            price=599.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1596194292724-9ca8389e2af5?w=800",
            stock=8
        ),
        Product(
            name="Soft Fabric Rolling Duffel",
            description="Large rolling duffel with reinforced base. Multiple grab handles and retractable tow handle.",
            price=139.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=24
        ),
        Product(
            name="Hardshell Cosmetic Case",
            description="Compact hardshell cosmetic case that matches our luggage line. Perfect for makeup and toiletries.",
            price=59.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1596969490001-f4e29c3e1a99?w=800",
            stock=42
        ),
        Product(
            name="Cabin Trolley Lightweight",
            description="Featherlight cabin trolley weighing only 4.2 lbs. Maximizes your packing capacity without adding weight.",
            price=129.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1589975876563-18d8a87e8c7e?w=800",
            stock=34
        ),
        Product(
            name="Premium Leather Wheeled Bag",
            description="Full-grain leather wheeled bag with vintage brass fittings. Combines classic style with modern functionality.",
            price=479.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1596194292724-9ca8389e2af5?w=800",
            stock=11
        ),
        Product(
            name="Sports Equipment Bag Wheeled",
            description="Oversized wheeled bag designed for sports equipment. Reinforced construction handles heavy loads.",
            price=169.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=19
        ),
        Product(
            name="Expandable Carry-On Pro",
            description="Expandable carry-on adds 2 inches when needed. Smart compartment design keeps items secure during expansion.",
            price=179.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1596969490001-f4e29c3e1a99?w=800",
            stock=31
        ),
        Product(
            name="Vintage Canvas Suitcase",
            description="Canvas exterior with leather trim. Nostalgic design with contemporary features. Perfect for style-conscious travelers.",
            price=249.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1604482423767-1bf5d6a2e566?w=800",
            stock=16
        ),
        Product(
            name="4-Wheel Spinner Medium",
            description="Medium-sized 4-wheel spinner perfect for week-long trips. Balanced capacity and maneuverability.",
            price=189.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1565026057447-bc90a3dceb87?w=800",
            stock=28
        ),
        Product(
            name="Fashion Forward Luggage",
            description="Trendy luggage with unique patterns and colors. Stand out at baggage claim with distinctive design.",
            price=169.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1585146777216-d05f72ce1ed5?w=800",
            stock=23
        ),
        Product(
            name="Executive Business Roller",
            description="Sophisticated business roller for the modern executive. Separate compartments for laptop, tablet, and documents.",
            price=259.99,
            category=ProductCategory.LUGGAGE.value,
            image_url="https://images.unsplash.com/photo-1622560480605-d83c853bc5c3?w=800",
            stock=20
        ),

        # BAGS - 30 items
        Product(
            name="Travel Backpack 40L",
            description="Versatile 40L travel backpack with laptop sleeve. Carry-on compliant size. Multiple access points and compression straps.",
            price=119.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=50
        ),
        Product(
            name="Crossbody Travel Bag",
            description="Anti-theft crossbody bag with RFID blocking pockets. Slash-proof construction and lockable zippers. Compact yet spacious.",
            price=59.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800",
            stock=60
        ),
        Product(
            name="Weekender Overnight Bag",
            description="Stylish weekender bag in faux leather. Separate shoe compartment and trolley sleeve. Perfect size for 2-3 day trips.",
            price=89.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=35
        ),
        Product(
            name="Gym Duffle with Shoe Compartment",
            description="Spacious gym duffle with ventilated shoe compartment. Water-resistant bottom. Adjustable shoulder strap and grab handles.",
            price=49.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=800",
            stock=42
        ),
        Product(
            name="Messenger Bag Canvas",
            description="Classic canvas messenger bag with leather accents. Padded laptop sleeve fits 15-inch. Adjustable shoulder strap.",
            price=79.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1573873911207-4817d5d00e4d?w=800",
            stock=38
        ),
        Product(
            name="Hiking Daypack 25L",
            description="Lightweight daypack perfect for hiking and day trips. Breathable back panel, hydration compatible. Multiple attachment points.",
            price=69.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1560174038-da43ac36a6b3?w=800",
            stock=45
        ),
        Product(
            name="Laptop Messenger Bag Professional",
            description="Professional leather messenger bag for business travelers. Organized compartments for laptop, tablet, and documents.",
            price=139.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?w=800",
            stock=28
        ),
        Product(
            name="Foldable Tote Bag",
            description="Ultra-light foldable tote that packs into itself. Perfect backup bag for shopping or beach. Water-resistant nylon.",
            price=24.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800",
            stock=70
        ),
        Product(
            name="Camera Backpack with Tripod Holder",
            description="Photographer's backpack with customizable dividers. Weather-resistant with rain cover. Tripod holder and quick-access side pocket.",
            price=159.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=22
        ),
        Product(
            name="Convertible Laptop Backpack",
            description="3-way convertible: backpack, briefcase, or messenger. TSA-friendly laptop compartment. USB charging port included.",
            price=99.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1585916420730-d7f95e942d43?w=800",
            stock=34
        ),
        Product(
            name="Toiletry Bag Hanging",
            description="Hanging toiletry bag with multiple compartments. Clear pockets for easy TSA screening. Hook for hanging in bathrooms.",
            price=34.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1586796676746-f15ab6c527f9?w=800",
            stock=55
        ),
        Product(
            name="Sling Bag Anti-Theft",
            description="Compact sling bag worn across chest. RFID protection and hidden pockets. Perfect for urban travel and commuting.",
            price=44.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800",
            stock=48
        ),
        Product(
            name="Beach Bag Waterproof",
            description="Large waterproof beach bag with zipper closure. Sand-resistant bottom. Multiple interior pockets for organization.",
            price=39.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800",
            stock=52
        ),
        Product(
            name="Business Laptop Backpack",
            description="Sleek business backpack with dedicated laptop and tablet compartments. Professional design suitable for office or travel.",
            price=109.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=40
        ),
        Product(
            name="Packable Daypack",
            description="Lightweight daypack that folds into its own pocket. Perfect for hiking, biking, or as an extra carry-on. Ultra-durable ripstop.",
            price=29.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1560174038-da43ac36a6b3?w=800",
            stock=65
        ),
        # Additional BAGS items
        Product(
            name="Leather Travel Tote",
            description="Elegant leather tote perfect for business travel. Fits laptop and documents. Professional appearance for meetings.",
            price=149.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800",
            stock=32
        ),
        Product(
            name="Waterproof Dry Bag 30L",
            description="Completely waterproof dry bag for water sports and outdoor adventures. Roll-top closure ensures contents stay dry.",
            price=54.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=41
        ),
        Product(
            name="Vintage Canvas Rucksack",
            description="Classic canvas rucksack with leather straps. Timeless design with modern durability. Multiple exterior pockets.",
            price=94.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1560174038-da43ac36a6b3?w=800",
            stock=28
        ),
        Product(
            name="Rolling Teacher Bag",
            description="Wheeled teacher bag with multiple compartments. Designed for educators on the move. Durable construction.",
            price=109.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=24
        ),
        Product(
            name="Tactical Molle Backpack",
            description="Military-grade tactical backpack with Molle attachments. Rugged 1000D nylon construction. Hydration compatible.",
            price=129.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1560174038-da43ac36a6b3?w=800",
            stock=36
        ),
        Product(
            name="Yoga Mat Carrier Bag",
            description="Specialized yoga mat bag with pockets for water bottle and accessories. Adjustable strap for comfort.",
            price=34.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800",
            stock=58
        ),
        Product(
            name="Insulated Lunch Bag",
            description="Insulated lunch bag keeps food fresh. Leak-proof lining and easy-clean interior. Perfect for work or travel.",
            price=24.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800",
            stock=67
        ),
        Product(
            name="Bike Messenger Bag Large",
            description="Large messenger bag designed for cyclists. Reflective strips for safety. Weather-resistant tarpaulin material.",
            price=89.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1573873911207-4817d5d00e4d?w=800",
            stock=31
        ),
        Product(
            name="Diaper Bag Backpack",
            description="Multi-functional diaper bag backpack for parents. Insulated pockets and changing pad included. Stylish unisex design.",
            price=79.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=44
        ),
        Product(
            name="Laptop Backpack Women's",
            description="Stylish laptop backpack designed for women. USB charging port and anti-theft pocket. Water-resistant fabric.",
            price=69.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=53
        ),
        Product(
            name="Clear Stadium Bag NFL Approved",
            description="Clear stadium bag compliant with NFL and concert venue policies. Multiple pockets with secure zippers.",
            price=19.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800",
            stock=82
        ),
        Product(
            name="Golf Shoe Bag",
            description="Ventilated golf shoe bag with separate compartments. Keeps shoes separate from clubs and clothes.",
            price=29.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800",
            stock=39
        ),
        Product(
            name="Rope Sling Backpack",
            description="Minimalist rope sling backpack for climbers and adventurers. Extremely lightweight and packable.",
            price=44.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1560174038-da43ac36a6b3?w=800",
            stock=47
        ),
        Product(
            name="Fishing Tackle Backpack",
            description="Specialized fishing backpack with tackle box compartments. Water-resistant base and multiple rod holders.",
            price=119.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=26
        ),
        Product(
            name="Picnic Backpack for 4",
            description="Complete picnic backpack with plates, cutlery, and insulated compartments. Perfect for outdoor dining.",
            price=99.99,
            category=ProductCategory.BAGS.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=22
        ),

        # TRAVEL_ACCESSORIES - 30 items
        Product(
            name="Travel Pillow Memory Foam",
            description="Ergonomic memory foam travel pillow with removable, washable cover. Provides neck support on planes, trains, and cars.",
            price=29.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1545987796-b199d6abb1b4?w=800",
            stock=80
        ),
        Product(
            name="Packing Cubes Set of 6",
            description="Complete packing cube set in various sizes. Mesh top for visibility. Compresses clothes and keeps luggage organized.",
            price=34.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=100
        ),
        Product(
            name="Luggage Scale Digital",
            description="Compact digital luggage scale with 110 lb capacity. Avoid overweight baggage fees. Backlit display and auto-off function.",
            price=14.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1566140967404-b8b3932483f5?w=800",
            stock=90
        ),
        Product(
            name="Travel Adapter Universal",
            description="All-in-one travel adapter works in 150+ countries. Includes USB-A and USB-C ports. Built-in surge protection.",
            price=39.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1591290619762-e02c4e82e3fe?w=800",
            stock=75
        ),
        Product(
            name="Compression Socks Travel",
            description="Compression socks for long flights. Improves circulation and reduces swelling. Available in multiple sizes and colors.",
            price=19.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1586202696648-d8f0e0e5b9d4?w=800",
            stock=120
        ),
        Product(
            name="RFID Blocking Passport Holder",
            description="Genuine leather passport holder with RFID blocking. Multiple card slots and document pockets. Protects against identity theft.",
            price=24.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1505682634904-d7c8d95cdc50?w=800",
            stock=85
        ),
        Product(
            name="Portable Luggage Lock TSA Approved",
            description="4-digit combination TSA-approved locks (set of 4). TSA agents can open without breaking. Includes reset instructions.",
            price=16.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1584460540867-d4b0091f3f7d?w=800",
            stock=110
        ),
        Product(
            name="Shoe Bags for Travel",
            description="Waterproof shoe bags with drawstring closure (set of 4). Separates shoes from clean clothes. Transparent window for easy identification.",
            price=12.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=95
        ),
        Product(
            name="Reusable Silicone Travel Bottles",
            description="TSA-approved silicone travel bottles for toiletries (set of 6). Leak-proof design. Wide opening for easy filling.",
            price=18.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=800",
            stock=88
        ),
        Product(
            name="Travel Blanket and Pillow Set",
            description="Compact travel blanket and pillow set in carrying pouch. Soft fleece material. Perfect for flights and road trips.",
            price=44.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1545987796-b199d6abb1b4?w=800",
            stock=62
        ),
        Product(
            name="Portable Door Lock",
            description="Portable security door lock for hotels and Airbnb. Easy installation without tools. Peace of mind while traveling.",
            price=21.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1584460540867-d4b0091f3f7d?w=800",
            stock=72
        ),
        Product(
            name="Microfiber Travel Towel Set",
            description="Quick-dry microfiber towel set (large and small). Super absorbent and compact. Comes with carrying pouch.",
            price=27.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1604522064454-07e2cd784a99?w=800",
            stock=78
        ),
        # Additional TRAVEL_ACCESSORIES items
        Product(
            name="Travel Jewelry Organizer",
            description="Compact jewelry organizer with multiple compartments. Prevents tangling and keeps valuables secure during travel.",
            price=26.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=64
        ),
        Product(
            name="Inflatable Foot Rest Travel",
            description="Inflatable foot rest for long flights. Reduces leg swelling and improves circulation. Compact when deflated.",
            price=22.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1545987796-b199d6abb1b4?w=800",
            stock=71
        ),
        Product(
            name="Luggage Tags Set Durable",
            description="Durable luggage tags with privacy flap (set of 5). Stainless steel loops won't fall off. Bright colors for easy identification.",
            price=15.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=98
        ),
        Product(
            name="Sleep Mask Silk with Earplugs",
            description="Premium silk sleep mask with contoured design. Includes noise-cancelling earplugs in travel case.",
            price=28.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1545987796-b199d6abb1b4?w=800",
            stock=83
        ),
        Product(
            name="Portable Clothesline Travel",
            description="Portable clothesline with 12 clips. Stretches up to 10 feet. Perfect for hand-washing clothes while traveling.",
            price=13.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=76
        ),
        Product(
            name="Travel Umbrella Compact Windproof",
            description="Compact umbrella fits in any bag. Windproof construction withstands strong gusts. Auto open/close button.",
            price=32.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1584460540867-d4b0091f3f7d?w=800",
            stock=69
        ),
        Product(
            name="Portable Luggage Cart Folding",
            description="Folding luggage cart supports up to 150 lbs. Compact design fits in suitcase. Extends to comfortable pulling height.",
            price=45.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=44
        ),
        Product(
            name="Neck Wallet Hidden Pocket",
            description="Hidden neck wallet for passport and cash. RFID blocking protection. Worn under clothing for security.",
            price=17.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1505682634904-d7c8d95cdc50?w=800",
            stock=91
        ),
        Product(
            name="Travel Laundry Bag Set",
            description="Set of 3 mesh laundry bags for organizing dirty clothes. Different colors for sorting. Machine washable.",
            price=16.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=87
        ),
        Product(
            name="Portable Safe Travel Lock Box",
            description="Portable safe with cable lock for securing valuables. Perfect for beaches, hostels, and hotels.",
            price=54.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1584460540867-d4b0091f3f7d?w=800",
            stock=38
        ),
        Product(
            name="Travel Sewing Kit Complete",
            description="Complete sewing kit in compact case. Includes thread, needles, buttons, and scissors. Emergency repairs on the go.",
            price=11.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=102
        ),
        Product(
            name="Portable Water Purifier Bottle",
            description="Water bottle with built-in purifier. Filters 99.99% of bacteria and parasites. Essential for international travel.",
            price=39.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=800",
            stock=56
        ),
        Product(
            name="Travel First Aid Kit Compact",
            description="Comprehensive first aid kit in compact case. Contains bandages, antiseptics, and essential medications.",
            price=24.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=73
        ),
        Product(
            name="Collapsible Water Bottle",
            description="Collapsible silicone water bottle. Rolls up when empty to save space. BPA-free and dishwasher safe.",
            price=18.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=800",
            stock=84
        ),
        Product(
            name="Travel Document Organizer Wallet",
            description="Complete document organizer holds passports, tickets, and cards. RFID protection for all pockets.",
            price=29.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1505682634904-d7c8d95cdc50?w=800",
            stock=79
        ),
        Product(
            name="Portable Steamer for Clothes",
            description="Compact travel steamer removes wrinkles quickly. Heats in 60 seconds. Dual voltage for international use.",
            price=42.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=47
        ),
        Product(
            name="Travel Mirror LED Lighted",
            description="Compact LED lighted mirror for makeup. Rechargeable battery lasts 2 weeks. Magnification option included.",
            price=34.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1600375739012-c09e0fef4b4e?w=800",
            stock=61
        ),
        Product(
            name="Luggage Strap with Scale",
            description="Luggage strap with integrated digital scale. Secure your bag and weigh it on the go. TSA-approved lock.",
            price=31.99,
            category=ProductCategory.TRAVEL_ACCESSORIES.value,
            image_url="https://images.unsplash.com/photo-1566140967404-b8b3932483f5?w=800",
            stock=52
        ),

        # DIGITAL_NOMAD - 30 items
        Product(
            name="Laptop Stand Portable Aluminum",
            description="Adjustable laptop stand folds flat for travel. Compatible with laptops up to 17 inches. Improves posture and airflow.",
            price=49.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1587614382346-4ec70e388b28?w=800",
            stock=55
        ),
        Product(
            name="Wireless Bluetooth Mouse",
            description="Compact wireless mouse with silent clicking. Works on any surface. Long battery life and auto-sleep function.",
            price=24.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1527814050087-3793815479db?w=800",
            stock=92
        ),
        Product(
            name="Portable Monitor 15.6 inch",
            description="USB-C portable monitor for dual-screen setup anywhere. Full HD IPS display. Includes protective case.",
            price=199.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800",
            stock=35
        ),
        Product(
            name="Noise Cancelling Headphones",
            description="Over-ear noise cancelling headphones with 30-hour battery. Perfect for working in cafes or coworking spaces.",
            price=179.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800",
            stock=48
        ),
        Product(
            name="Power Bank 20000mAh",
            description="High-capacity power bank with fast charging. Charges phone 4-6 times. Multiple USB ports for charging multiple devices.",
            price=49.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=800",
            stock=70
        ),
        Product(
            name="Mechanical Keyboard Compact",
            description="60% compact mechanical keyboard. Bluetooth and wired connectivity. Portable without sacrificing typing experience.",
            price=89.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800",
            stock=42
        ),
        Product(
            name="Webcam 1080p HD",
            description="HD webcam with autofocus and low-light correction. Built-in microphone. Perfect for video calls while traveling.",
            price=69.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1588421357574-87938a86fa28?w=800",
            stock=58
        ),
        Product(
            name="Cable Organizer Kit",
            description="Complete cable management solution for digital nomads. Multiple pouches and elastic bands. Keeps tech gear organized.",
            price=22.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1591290619762-e02c4e82e3fe?w=800",
            stock=105
        ),
        Product(
            name="Ergonomic Wireless Keyboard and Mouse",
            description="Ergonomic keyboard and mouse combo. Wireless connectivity with single USB receiver. Designed for all-day comfort.",
            price=79.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800",
            stock=64
        ),
        Product(
            name="USB-C Hub 7-in-1",
            description="7-in-1 USB-C hub with HDMI, USB 3.0, SD card reader, and Ethernet. Essential for laptops with limited ports.",
            price=44.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1625948515291-69613efd103f?w=800",
            stock=82
        ),
        Product(
            name="Blue Light Blocking Glasses",
            description="Computer glasses that block blue light. Reduces eye strain during long work sessions. Stylish lightweight frame.",
            price=29.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1577803645773-f96470509666?w=800",
            stock=76
        ),
        Product(
            name="Phone Stand Adjustable",
            description="Adjustable phone and tablet stand. Sturdy aluminum construction. Perfect for video calls or watching content.",
            price=19.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=800",
            stock=88
        ),
        Product(
            name="Laptop Sleeve 13-14 inch",
            description="Padded laptop sleeve with extra pocket for accessories. Water-resistant exterior. Slim design fits in backpacks.",
            price=34.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1601524909162-ae8725290836?w=800",
            stock=95
        ),
        # Additional DIGITAL_NOMAD items
        Product(
            name="Portable SSD 1TB External",
            description="Ultra-fast portable SSD with 1TB capacity. USB-C connection. Shock-resistant for travel durability.",
            price=129.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1531492746076-161ca9bcad58?w=800",
            stock=67
        ),
        Product(
            name="Wireless Keyboard Foldable",
            description="Foldable Bluetooth keyboard fits in pocket. Compatible with all devices. Rechargeable battery lasts months.",
            price=59.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800",
            stock=54
        ),
        Product(
            name="USB-C to Everything Adapter",
            description="Universal USB-C adapter with HDMI, VGA, USB-A, and Ethernet. Single solution for all connections.",
            price=54.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1625948515291-69613efd103f?w=800",
            stock=71
        ),
        Product(
            name="Portable WiFi Hotspot Global",
            description="Global WiFi hotspot works in 130+ countries. No SIM card needed. Connects up to 10 devices.",
            price=149.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1606904825846-647eb07f5be2?w=800",
            stock=43
        ),
        Product(
            name="Wireless Presentation Clicker",
            description="Professional presentation remote with laser pointer. Bluetooth connectivity up to 100 feet range.",
            price=34.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1527814050087-3793815479db?w=800",
            stock=62
        ),
        Product(
            name="Laptop Privacy Screen 15.6",
            description="Privacy screen filter for 15.6-inch laptops. Blocks side viewing angles. Anti-glare coating included.",
            price=39.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1587614382346-4ec70e388b28?w=800",
            stock=58
        ),
        Product(
            name="Streaming Ring Light Portable",
            description="Portable ring light with adjustable brightness. Perfect for video calls and content creation. USB powered.",
            price=44.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1588421357574-87938a86fa28?w=800",
            stock=49
        ),
        Product(
            name="Wireless Earbuds Pro",
            description="Premium wireless earbuds with active noise cancellation. 30-hour total battery life with charging case.",
            price=159.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=800",
            stock=73
        ),
        Product(
            name="Laptop Cooling Pad RGB",
            description="Laptop cooling pad with 5 quiet fans. RGB lighting effects. Ergonomic angle adjustment.",
            price=49.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1587614382346-4ec70e388b28?w=800",
            stock=56
        ),
        Product(
            name="Portable Document Scanner",
            description="Portable scanner digitizes documents on the go. WiFi enabled. Scan to cloud or USB directly.",
            price=199.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1588421357574-87938a86fa28?w=800",
            stock=34
        ),
        Product(
            name="Smart Notebook Digital Reusable",
            description="Reusable smart notebook syncs handwritten notes to cloud. Microwave to erase pages. Includes app.",
            price=34.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1531346878377-a5be20888e57?w=800",
            stock=81
        ),
        Product(
            name="Wireless Trackpad Precision",
            description="Multi-touch wireless trackpad with gesture support. Rechargeable battery. Works with all operating systems.",
            price=64.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1527814050087-3793815479db?w=800",
            stock=47
        ),
        Product(
            name="Vertical Laptop Stand Dual",
            description="Vertical stand holds two laptops. Adjustable width. Saves desk space in coworking environments.",
            price=29.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1587614382346-4ec70e388b28?w=800",
            stock=68
        ),
        Product(
            name="USB-C Docking Station 12-in-1",
            description="Ultimate 12-in-1 docking station. Dual HDMI, Ethernet, SD/microSD, USB 3.0 ports. Powers laptop up to 100W.",
            price=119.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1625948515291-69613efd103f?w=800",
            stock=52
        ),
        Product(
            name="Portable Printer Wireless",
            description="Compact wireless printer for mobile printing. Battery powered. Prints from phone or laptop.",
            price=179.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1588421357574-87938a86fa28?w=800",
            stock=28
        ),
        Product(
            name="Monitor Light Bar",
            description="LED light bar mounts on monitor. Reduces eye strain. USB powered with touch controls.",
            price=49.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1565373679610-a0e892f66333?w=800",
            stock=63
        ),
        Product(
            name="Laptop Backpack with Charging Station",
            description="Tech backpack with built-in power bank and charging cables. Organized compartments for all devices.",
            price=89.99,
            category=ProductCategory.DIGITAL_NOMAD.value,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
            stock=41
        ),
    ]

    # Add all products to database
    db.add_all(products)
    db.commit()

    print(f"Successfully seeded {len(products)} products!")
    print(f"  - Luggage: {len([p for p in products if p.category == ProductCategory.LUGGAGE.value])}")
    print(f"  - Bags: {len([p for p in products if p.category == ProductCategory.BAGS.value])}")
    print(f"  - Travel Accessories: {len([p for p in products if p.category == ProductCategory.TRAVEL_ACCESSORIES.value])}")
    print(f"  - Digital Nomad: {len([p for p in products if p.category == ProductCategory.DIGITAL_NOMAD.value])}")


def main():
    """Main function to run the seed script."""
    print("Initializing database...")
    init_db()

    print("Starting product seed...")
    db = SessionLocal()
    try:
        seed_products(db)
    except Exception as e:
        print(f"Error seeding products: {e}")
        db.rollback()
    finally:
        db.close()

    print("Seed complete!")


if __name__ == "__main__":
    main()
