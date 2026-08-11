lots_corp_version = "Version 1.0"

f"""
=========================================================
LOTS Corp.
Synthetic ERP Dataset Generator
{lots_corp_version}
=========================================================

"""
from datetime import timedelta
from pathlib import Path
from faker import Faker
from datetime import datetime
import random
import re

import pandas as pd
import numpy as np
import calendar

fake = Faker("en_PH")

# ------------------------------------------------------
# Random Seed
# ------------------------------------------------------

random.seed(42)
TODAY = pd.Timestamp.today().date()

# ======================================================
# LOTS Corp Timeline
# ======================================================

COMPANY_FOUNDING_DATE = pd.to_datetime("2021/1/1").date()

# ------------------------------------------------------
# Project Folders
# ------------------------------------------------------

BASE_DIR = Path(__file__).parent

RAW_DIR = BASE_DIR / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)




# ------------------------------------------------------
# Philippine Mobile Generator
# ------------------------------------------------------

PH_MOBILE_PREFIXES = [
    "0917",
    "0918",
    "0919",
    "0920",
    "0921",
    "0928",
    "0935",
    "0945",
    "0956",
    "0966",
    "0977",
    "0981",
    "0998"
]

# ======================================================
# Orders Configuration
# ======================================================

ORDER_COUNT = 500_000 #5_000

ORDER_START_DATE = pd.to_datetime("2024/1/1").date()

ORDER_END_DATE = TODAY


PAYMENT_METHODS = {

    "Credit Terms": 60,

    "Bank Transfer": 30,

    "Cash": 10

}

# ======================================================
# Customer Order Activity
# ======================================================

CUSTOMER_ACTIVITY = {

    "High": 15,

    "Medium": 35,

    "Low": 50

}

# ======================================================
# Annual Order Frequency
# ======================================================

ORDER_FREQUENCY = {

    "High": (40, 90),

    "Medium": (12, 39),

    "Low": (1, 11)

}

# ======================================================
# Sales Representative Order Capacity
# ======================================================

SALES_REP_ORDER_CAPACITY = {

    "High": (650, 900),

    "Medium": (400, 649),

    "Low": (150, 399)

}

# ======================================================
# Sales Representative Capacity
# ======================================================

SALES_REP_ACTIVITY = {

    "High": 20,

    "Medium": 50,

    "Low": 30

}

# ======================================================
# Transaction Date Configuration
# ======================================================

DATASET_END_DATE = pd.to_datetime(pd.Timestamp.today().date())

MONTHLY_ORDER_WEIGHTS = {

    1: 12,
    2: 8,
    3: 8,
    4: 5,
    5: 8,
    6: 11,
    7: 8,
    8: 8,
    9: 10,
    10: 11,
    11: 13,
    12: 14

}

# ======================================================
# Customer Purchase Behavior
# ======================================================

PURCHASE_FREQUENCY = {

    "High": 0.70,

    "Medium": 1.00,

    "Low": 1.40

}

PURCHASE_INTERVAL_VARIATION = {

    "High": 3,

    "Medium": 6,

    "Low": 10

}

ORDER_TIMELINE_RULES = {

    "High": {

        "minimum_gap": 2,

        "variation_factor": 0.25

    },

    "Medium": {

        "minimum_gap": 5,

        "variation_factor": 0.25

    },

    "Low": {

        "minimum_gap": 10,

        "variation_factor": 0.25

    }

}

ORDER_STATUS_RULES = {

    "Recent": {

        "max_days": 7,

        "weights": {

            "Processing": 60,

            "Shipped": 30,

            "Cancelled": 5,

            "Delivered": 5

        }

    },

    "Active": {

        "max_days": 30,

        "weights": {

            "Delivered": 45,

            "Shipped": 35,

            "Processing": 15,

            "Cancelled": 5

        }

    },

    "Mature": {

        "max_days": 90,

        "weights": {

            "Delivered": 82,

            "Shipped": 10,

            "Cancelled": 5,

            "Returned": 3

        }

    },

    "Historical": {

        "max_days": float("inf"),

        "weights": {

            "Delivered": 90,

            "Returned": 4,

            "Cancelled": 6

        }

    }

}

PAYMENT_STATUS_RULES = {

    "Processing": {

        "Pending": 95,

        "Paid": 5

    },

    "Shipped": {

        "Pending": 60,

        "Paid": 40

    },

    "Delivered": {

        "Paid": 96,

        "Pending": 3,

        "Overdue": 1

    },

    "Returned": {

        "Refunded": 90,

        "Paid": 10

    },

    "Cancelled": {

        "Cancelled": 100

    }

}

ORDER_SOURCE = {

    "Sales Representative": 72,

    "Phone": 12,

    "Email": 10,

    "Walk-in": 4,

    "Website": 2

}

PRODUCT_SALES_WEIGHTS = {

    # ------------------------------------------
    # Accessories
    # ------------------------------------------

    "Wireless Mouse": 20,
    "Wireless Keyboard": 18,
    "USB Hub": 16,
    "Webcam": 12,
    "Headset": 15,
    "Laptop Backpack": 10,
    "Docking Station": 8,
    "HDMI Cable": 25,
    "USB Flash Drive": 22,

    # ------------------------------------------
    # Desktop
    # ------------------------------------------

    "Business Desktop": 8,
    "Compact Desktop": 6,
    "Workstation Desktop": 3,
    "Mini PC": 5,
    "All-in-One Desktop": 4,

    # ------------------------------------------
    # Laptop
    # ------------------------------------------

    "Business Laptop": 10,
    "Ultrabook": 7,
    "Engineering Laptop": 4,
    "Budget Laptop": 8,
    "Executive Laptop": 5,
    "2-in-1 Laptop": 3,
    "Mobile Workstation": 2,
    "Chromebook": 4,

    # ------------------------------------------
    # Monitor
    # ------------------------------------------

    "24-inch Monitor": 12,
    "27-inch Monitor": 9,
    "Ultrawide Monitor": 3,
    "4K Monitor": 2,

    # ------------------------------------------
    # Networking
    # ------------------------------------------

    "Wi-Fi Router": 10,
    "Network Switch": 8,
    "Access Point": 6,
    "Ethernet Cable": 24,
    "Patch Panel": 5,
    "Network Rack": 2,

    # ------------------------------------------
    # Office Equipment
    # ------------------------------------------

    "Paper Shredder": 5,
    "Laminating Machine": 3,
    "Binding Machine": 2,
    "Document Scanner": 7,
    "Label Printer": 4,

    # ------------------------------------------
    # Printer
    # ------------------------------------------

    "Inkjet Printer": 8,
    "Laser Printer": 9,
    "Multifunction Printer": 7,
    "Receipt Printer": 4,
    "Dot Matrix Printer": 1,

    # ------------------------------------------
    # Storage
    # ------------------------------------------

    "External HDD": 12,
    "External SSD": 15,
    "Internal SSD": 14,
    "NAS Storage": 3,
    "Memory Card": 10,
    "Portable SSD": 13,
    "USB Drive Enterprise": 8,
    "Backup Drive": 7

}

# ------------------------------------------------------
# Supplier Master List
# ------------------------------------------------------

SUPPLIERS = [
    ("PrimeSource Office Supplies Inc.", "primesourceoffice"),
    ("MetroTech Distribution Corporation", "metrotechdistribution"),
    ("Vertex Industrial Traders", "vertexindustrial"),
    ("Golden Axis Business Solutions", "goldenaxis"),
    ("Pacific Office Essentials", "pacificoffice"),
    ("NorthPeak Technology Supply", "northpeaktech"),
    ("Alliance Office Products", "allianceoffice"),
    ("Pinnacle Distribution Group", "pinnacledg"),
    ("EastBridge Business Supply", "eastbridge"),
    ("BluePeak Office Systems", "bluepeak"),
    ("Sterling Office Supply", "sterlingoffice"),
    ("Horizon Business Solutions", "horizonbiz"),
    ("ExcelPro Distribution", "excelpro"),
    ("Optimum Tech Traders", "optimumtech"),
    ("Summit Industrial Supply", "summitindustrial"),
    ("CoreLink Office Products", "corelink"),
    ("NextWave Distribution", "nextwave"),
    ("Unity Business Essentials", "unitybusiness"),
]

# ------------------------------------------------------
# Filipino First Names
# ------------------------------------------------------

FIRST_NAMES = [
    "Frances",
    "John Paul",
    "Maria",
    "Carlo",
    "Jessa",
    "Angela",
    "Rafael",
    "Paolo",
    "Mark",
    "Joan",
    "Kristine",
    "Michael",
    "Rose",
    "Kevin",
    "Nicole",
    "Joshua",
    "Patricia",
    "Daniel",
    "Christian",
    "Joy",
    "Kenneth",
    "Princess",
    "Kim",
    "Jerome",
    "Sheila",
    "Ryan",
    "Alyssa",
    "Vincent",
    "Marvin",
    "Louise"
]

# ------------------------------------------------------
# Filipino Last Names
# ------------------------------------------------------

LAST_NAMES = [
    "Santos",
    "Reyes",
    "Garcia",
    "Cruz",
    "Mendoza",
    "Torres",
    "Villanueva",
    "Ramos",
    "Aquino",
    "Bautista",
    "Navarro",
    "Castillo",
    "Domingo",
    "Fernandez",
    "Salazar",
    "Cardenas",
    "Flores",
    "Rivera",
    "Dela Cruz",
    "Soriano",
    "Lopez",
    "Valdez",
    "Rosales",
    "De Leon",
    "Manalo",
    "Evangelista",
    "Pascual",
    "Mercado",
    "Santiago",
    "Del Rosario"
]

# ======================================================
# Filipino First Names
# ======================================================

FILIPINO_FIRST_NAMES = [

    # Male
    "Aaron",
    "Adrian",
    "Albert",
    "Alex",
    "Alvin",
    "Anthony",
    "Arvin",
    "Ben",
    "Carlo",
    "Christian",
    "Christopher",
    "Daniel",
    "David",
    "Dennis",
    "Edgar",
    "Emmanuel",
    "Eric",
    "Francis",
    "Gabriel",
    "Gerald",
    "Ian",
    "Jerome",
    "John",
    "Jonathan",
    "Joseph",
    "Joshua",
    "Kevin",
    "Kenneth",
    "Mark",
    "Marvin",
    "Michael",
    "Nathan",
    "Paolo",
    "Patrick",
    "Paul",
    "Rafael",
    "Ramon",
    "Raymond",
    "Richard",
    "Ryan",
    "Samuel",
    "Vincent",

    # Female
    "Angela",
    "Angelica",
    "Anne",
    "April",
    "Bea",
    "Bernadette",
    "Camille",
    "Carla",
    "Catherine",
    "Christine",
    "Daisy",
    "Elaine",
    "Erika",
    "Grace",
    "Hazel",
    "Irene",
    "Janelle",
    "Janine",
    "Jasmine",
    "Jenny",
    "Jessica",
    "Joy",
    "Julia",
    "Karen",
    "Katherine",
    "Kristine",
    "Liza",
    "Lovely",
    "Maria",
    "Maricel",
    "Michelle",
    "Nicole",
    "Patricia",
    "Princess",
    "Rose",
    "Shiela",
    "Sophia",
    "Theresa",
    "Vanessa"
]

FILIPINO_LAST_NAMES = [

    "Abad",
    "Aguilar",
    "Aquino",
    "Bautista",
    "Castro",
    "Cruz",
    "De Guzman",
    "De Leon",
    "De Vera",
    "Dela Cruz",
    "Domingo",
    "Flores",
    "Garcia",
    "Gonzales",
    "Hernandez",
    "Luna",
    "Mendoza",
    "Navarro",
    "Ocampo",
    "Pascual",
    "Reyes",
    "Rivera",
    "Ramos",
    "Romero",
    "Salazar",
    "Santiago",
    "Santos",
    "Soriano",
    "Torres",
    "Valdez",
    "Villanueva"
]

# ------------------------------------------------------
# Philippine Locations
# ------------------------------------------------------

LOCATIONS = [
    ("NCR", "Metro Manila", "Makati"),
    ("NCR", "Metro Manila", "Taguig"),
    ("NCR", "Metro Manila", "Pasig"),
    ("NCR", "Metro Manila", "Quezon City"),
    ("CALABARZON", "Laguna", "Santa Rosa"),
    ("CALABARZON", "Laguna", "Calamba"),
    ("CALABARZON", "Cavite", "Dasmariñas"),
    ("Central Luzon", "Bulacan", "Malolos"),
    ("Central Luzon", "Pampanga", "San Fernando"),
    ("Central Visayas", "Cebu", "Cebu City"),
    ("Western Visayas", "Iloilo", "Iloilo City"),
    ("Davao Region", "Davao del Sur", "Davao City")
]

# ------------------------------------------------------
# Business Rules
# ------------------------------------------------------

PAYMENT_TERMS = [
    "Cash",
    "Net 15",
    "Net 30",
    "Net 45"
]

SUPPLIER_STATUS = [
    "Active",
    "Inactive"
]

# ======================================================
# PRODUCT CONFIGURATION
# ======================================================

# ------------------------------------------------------
# Brand Tier Multipliers
# ------------------------------------------------------

BRAND_MULTIPLIERS = {

    "Apex": 1.18,
    "Nova": 1.00,
    "VisionView": 1.05,
    "DataVault": 1.02,
    "SwiftLink": 1.03,
    "CorePrint": 1.00,
    "FlexPoint": 0.90,
    "OfficePro": 0.92

}


# ------------------------------------------------------
# Cost Price Ranges (PHP)
# ------------------------------------------------------

FAMILY_BASE_PRICE = {

    # -----------------------------
    # Laptop
    # -----------------------------

    "ApexBook Essential": 28000,
    "ApexBook Pro": 42000,
    "NovaBook Air": 34000,
    "NovaBook Ultra": 56000,

    # -----------------------------
    # Desktop
    # -----------------------------

    "ApexStation": 31000,
    "NovaStation": 36000,

    # -----------------------------
    # Monitor
    # -----------------------------

    "VisionView Essential": 5200,
    "VisionView Pro": 7800,
    "VisionView Ultra": 12000,

    # -----------------------------
    # Storage
    # -----------------------------

    "DataVault SSD": 2800,
    "DataVault HDD": 3300,
    "DataVault FlashDrive": 450,

    # -----------------------------
    # Networking
    # -----------------------------

    "SwiftLink Router": 3500,
    "SwiftLink Switch": 4200,
    "SwiftLink Access Point": 3900,

    # -----------------------------
    # Printer
    # -----------------------------

    "CorePrint InkJet": 5200,
    "CorePrint Laser": 9800,
    "CorePrint Label": 6500,

    # -----------------------------
    # Accessories
    # -----------------------------

    "FlexMouse": 550,
    "FlexKeyboard": 850,
    "FlexHeadset": 1350,
    "FlexWebcam": 1800,
    "FlexHub": 950,

    # -----------------------------
    # Office Equipment
    # -----------------------------

    "OfficePro Shredder": 4200,
    "OfficePro Laminator": 2800,
    "OfficePro Binding Machine": 3600,
    "OfficePro Projector": 18500,
    "OfficePro Document Scanner": 9800
}

# ------------------------------------------------------
# Gross Markup %
# ------------------------------------------------------

CATEGORY_MARKUP_RANGES = {

    "Laptop": (0.18, 0.30),

    "Desktop": (0.18, 0.30),

    "Monitor": (0.20, 0.35),

    "Storage": (0.25, 0.40),

    "Networking": (0.25, 0.40),

    "Printer": (0.20, 0.35),

    "Accessories": (0.40, 0.80),

    "Office Equipment": (0.30, 0.60)

}


# ------------------------------------------------------
# Product Status
# ------------------------------------------------------

PRODUCT_STATUS = [

    True,
    False

]


# ------------------------------------------------------
# Supplier Specialization
# ------------------------------------------------------

SUPPLIER_CATEGORY = {

    "MetroTech Distribution Corporation":
        ["Laptop"],

    "Summit Industrial Supply":
        ["Laptop"],

    "Golden Axis Business Solutions":
        ["Desktop"],

    "Pinnacle Distribution Group":
        ["Monitor"],

    "BluePeak Office Systems":
        ["Monitor"],

    "NorthPeak Technology Supply":
        ["Storage"],

    "Optimum Tech Traders":
        ["Storage"],

    "Vertex Industrial Traders":
        ["Networking"],

    "Horizon Business Solutions":
        ["Networking"],

    "Alliance Office Products":
        ["Printer"],

    "ExcelPro Distribution":
        ["Printer"],

    "Pacific Office Essentials":
        ["Accessories"],

    "EastBridge Business Supply":
        ["Accessories"],

    "CoreLink Office Products":
        ["Accessories"],

    "PrimeSource Office Supplies Inc.":
        ["Office Equipment"],

    "Sterling Office Supply":
        ["Office Equipment"],

    "Unity Business Essentials":
        ["Office Equipment"]

}

# ======================================================
# PRODUCT MASTER FAMILIES
# ======================================================

PRODUCT_FAMILIES = [

    # ==================================================
    # STORAGE
    # ==================================================

    {
        "brand": "DataVault",
        "family": "DataVault SSD",
        "category": "Storage",
        "variants": [

            {
                "name": "256GB",
                "factor": 1.00
            },
            {
                "name": "512GB",
                "factor": 1.5
            },
            {
                "name": "1TB",
                "factor": 2.00
            }

        ],
        "supplier": "NorthPeak Technology Supply",
        "description":
            "High-speed solid-state drive for desktops and laptops."
    },

    {
        "brand": "DataVault",
        "family": "DataVault HDD",
        "category": "Storage",
        "variants": [

            {
                "name": "1TB",
                "factor": 1.00
            },
            {
                "name": "2TB",
                "factor": 1.5
            },
            {
                "name": "4TB",
                "factor": 2.00
            }

        ],
        "supplier": "Optimum Tech Traders",
        "description":
            "Reliable hard disk drive for business storage."
    },

    {
        "brand": "DataVault",
        "family": "DataVault FlashDrive",
        "category": "Storage",
        "variants": [

            {
                "name": "32GB",
                "factor": 1.00
            },
            {
                "name": "64GB",
                "factor": 1.5
            }

        ],
        "supplier": "NorthPeak Technology Supply",
        "description":
            "Portable USB flash storage for everyday file transfer."
    },

    # ==================================================
    # NETWORKING
    # ==================================================

    {
        "brand": "SwiftLink",
        "family": "SwiftLink Router",
        "category": "Networking",
        "variants": [

            {
                "name": "AC1200",
                "factor": 1.00
            },
            {
                "name": "AX1800",
                "factor": 1.2
            }

        ],
        "supplier": "Vertex Industrial Traders",
        "description":
            "Wireless router designed for office connectivity."
    },

    {
        "brand": "SwiftLink",
        "family": "SwiftLink Switch",
        "category": "Networking",
        "variants": [

            {
                "name": "8-Port",
                "factor": 1.00
            },
            {
                "name": "16-Port",
                "factor": 1.5
            }

        ],
        "supplier": "Horizon Business Solutions",
        "description":
            "Managed network switch for office infrastructure."
    },

    {
        "brand": "SwiftLink",
        "family": "SwiftLink Access Point",
        "category": "Networking",
        "variants": [

            {
                "name": "Indoor",
                "factor": 1.00
            },
            {
                "name": "Outdoor",
                "factor": 1.5
            }

        ],
        "supplier": "Vertex Industrial Traders",
        "description":
            "Business-grade wireless access point."
    },

    # ==================================================
    # PRINTERS
    # ==================================================

    {
        "brand": "CorePrint",
        "family": "CorePrint InkJet",
        "category": "Printer",
        "variants": [

            {
                "name": "Color",
                "factor": 1.00
            }

        ],
        "supplier": "Alliance Office Products",
        "description":
            "Color inkjet printer for office documents."
    },

    {
        "brand": "CorePrint",
        "family": "CorePrint Laser",
        "category": "Printer",
        "variants": [

            {
                "name": "Mono",
                "factor": 1.00
            },
            {
                "name": "Color",
                "factor": 1.5
            }

        ],
        "supplier": "ExcelPro Distribution",
        "description":
            "Laser printer designed for business environments."
    },

    {
        "brand": "CorePrint",
        "family": "CorePrint Label",
        "category": "Printer",
        "variants": [

            {
                "name": "Standard",
                "factor": 1.00
            },
            {
                "name": "Industrial",
                "factor": 1.5
            }

        ],
        "supplier": "Alliance Office Products",
        "description":
            "Label printer for warehouse and inventory operations."
    },

    # ==================================================
    # ACCESSORIES
    # ==================================================

    {
        "brand": "FlexPoint",
        "family": "FlexMouse",
        "category": "Accessories",
        "variants": [

            
            {
                "name": "Wired",
                "factor": 1.00
            },
            {
                "name": "Wireless",
                "factor": 1.5
            }

        ],
        "supplier": "Pacific Office Essentials",
        "description":
            "Optical mouse for office productivity."
    },

    {
        "brand": "FlexPoint",
        "family": "FlexKeyboard",
        "category": "Accessories",
        "variants": [

            {
                "name": "Wired",
                "factor": 1.00
            },
            {
                "name": "Wireless",
                "factor": 1.5
            }

        ],
        "supplier": "EastBridge Business Supply",
        "description":
            "Full-size keyboard designed for everyday office work."
    },

    {
        "brand": "FlexPoint",
        "family": "FlexHeadset",
        "category": "Accessories",
        "variants": [

            {
                "name": "USB",
                "factor": 1.00
            },
            {
                "name": "Bluetooth",
                "factor": 1.5
            }

        ],
        "supplier": "CoreLink Office Products",
        "description":
            "Headset for meetings and online collaboration."
    },

    {
        "brand": "FlexPoint",
        "family": "FlexWebcam",
        "category": "Accessories",
        "variants": [

            {
                "name": "HD",
                "factor": 1.00
            },
            {
                "name": "Full HD",
                "factor": 1.5
            }

        ],
        "supplier": "Pacific Office Essentials",
        "description":
            "USB webcam for video conferencing."
    },

    {
        "brand": "FlexPoint",
        "family": "FlexHub",
        "category": "Accessories",
        "variants": [

            {
                "name": "4-Port",
                "factor": 1.00
            }

        ],
        "supplier": "CoreLink Office Products",
        "description":
            "USB hub for connecting multiple peripherals."
    },

    # ==================================================
    # OFFICE EQUIPMENT
    # ==================================================

    {
        "brand": "OfficePro",
        "family": "OfficePro Shredder",
        "category": "Office Equipment",
        "variants": [

            {
                "name": "Personal",
                "factor": 1.00
            }

        ],
        "supplier": "PrimeSource Office Supplies Inc.",
        "description":
            "Paper shredder for secure document disposal."
    },

    {
        "brand": "OfficePro",
        "family": "OfficePro Laminator",
        "category": "Office Equipment",
        "variants": [

            {
                "name": "A4",
                "factor": 1.00
            }

        ],
        "supplier": "Sterling Office Supply",
        "description":
            "Document laminator for office use."
    },

    {
        "brand": "OfficePro",
        "category": "Office Equipment",
        "family": "OfficePro Binding Machine",
        "variants": [

            {
                "name": "Comb",
                "factor": 1.00
            }

        ],
        "supplier": "Unity Business Essentials",
        "description":
            "Binding machine for reports and presentations."
    },

    {
        "brand": "OfficePro",
        "family": "OfficePro Projector",
        "category": "Office Equipment",
        "variants": [

            {
                "name": "Business",
                "factor": 1.00
            }

        ],
        "supplier": "PrimeSource Office Supplies Inc.",
        "description":
            "Business projector for meetings and presentations."
    },

    {
        "brand": "OfficePro",
        "family": "OfficePro Document Scanner",
        "category": "Office Equipment",
        "variants": [

            {
                "name": "ADF",
                "factor": 1.00
            }

        ],
        "supplier": "PrimeSource Office Supplies Inc.",
        "description":
            "Automatic document scanner for business document digitization."
    },

    # ==================================================
    # LAPTOPS
    # ==================================================

    {
        "brand": "Apex",
        "family": "ApexBook Essential",
        "category": "Laptop",
        "variants": [

            {
                "name": "12-inch",
                "factor": 1.00
            },
            {
                "name": "13-inch",
                "factor": 1.1
            }

        ],
        "supplier": "MetroTech Distribution Corporation",
        "description":
            "Business laptop designed for office productivity."
    },

    {
        "brand": "Apex",
        "family": "ApexBook Pro",
        "category": "Laptop",
        "variants": [

            {
                "name": "14-inch",
                "factor": 1.00
            },
            {
                "name": "16-inch",
                "factor": 1.2
            }

        ],
        "supplier": "MetroTech Distribution Corporation",
        "description":
            "Business laptop designed for office productivity."
    },

    {
        "brand": "Nova",
        "family": "NovaBook Air",
        "category": "Laptop",
        "variants": [

            
            {
                "name": "14-inch",
                "factor": 1.00
            },
            {
                "name": "16-inch",
                "factor": 1.2
            }

        ],
        "supplier": "Summit Industrial Supply",
        "description":
            "Reliable laptop for business and everyday work."
    },

    {
        "brand": "Nova",
        "family": "NovaBook Ultra",
        "category": "Laptop",
        "variants": [

            {
                "name": "16-inch",
                "factor": 1.00
            },
            {
                "name": "18-inch",
                "factor": 1.2
            }

        ],
        "supplier": "Summit Industrial Supply",
        "description":
            "Reliable laptop for business and everyday work."
    },

    # ==================================================
    # DESKTOPS
    # ==================================================

    {
        "brand": "Nova",
        "family": "NovaStation",
        "category": "Desktop",
        "variants": [

            {
                "name": "Mini",
                "factor": 1.00
            },
            {
                "name": "Tower",
                "factor": 1.5
            },
            {
                "name": "Workstation",
                "factor": 1.8
            }
 
        ],
        "supplier": "Golden Axis Business Solutions",
        "description":
            "Compact desktop computer for office environments."
    },

    {
        "brand": "Apex",
        "family": "ApexStation",
        "category": "Desktop",
        "variants": [

            {
                "name": "Pro",
                "factor": 1.00
            },
            {
                "name": "Compact",
                "factor": 1.5
            }

        ],
        "supplier": "Golden Axis Business Solutions",
        "description":
            "High-performance desktop workstation."
    },

    # ==================================================
    # MONITORS
    # ==================================================

    {
        "brand":"VisionView",
        "family":"VisionView Essential",
        "category":"Monitor",
        "variants":[

            {
                "name": "24-inch",
                "factor": 1.00
            },
            {
                "name": "27-inch",
                "factor": 1.1
            }

        ],
        "supplier":"Pinnacle Distribution Group",
        "description":
            "Professional IPS monitor."
    },

    {
        "brand":"VisionView",
        "family":"VisionView Pro",
        "category":"Monitor",
        "variants":[

            {
                "name": "32-inch",
                "factor": 1.00
            }

        ],
        "supplier":"BluePeak Office Systems",
        "description":
            "Office monitor for daily productivity."
    },
    {
        "brand":"VisionView",
        "family":"VisionView Ultra",
        "category":"Monitor",
        "variants":[

            {
                "name": "42-inch",
                "factor": 1.00
            }

        ],
        "supplier":"BluePeak Office Systems",
        "description":
            "Office monitor for daily productivity."
    },

]

# ======================================================
# CUSTOMER CONFIGURATION
# ======================================================

TOTAL_CUSTOMERS = 300

CUSTOMER_TYPES = {
    "Corporate": 40,
    "Retail Business": 20,
    "Education": 12,
    "Government": 10,
    "Healthcare": 8,
    "Manufacturing": 10
}

INDUSTRIES = {

    "Corporate": [
        "Information Technology",
        "Consulting",
        "Accounting Services",
        "Engineering",
        "Logistics",
        "Telecommunications"
    ],

    "Retail Business": [
        "Computer Store",
        "Office Supplies",
        "Electronics",
        "Furniture",
        "Supermarket"
    ],

    "Education": [
        "University",
        "College",
        "Academy",
        "Training Center"
    ],

    "Government": [
        "City Government",
        "Municipal Government",
        "National Agency",
        "Public School District"
    ],

    "Healthcare": [
        "Hospital",
        "Medical Clinic",
        "Diagnostic Center"
    ],

    "Manufacturing": [
        "Food Manufacturing",
        "Electronics Manufacturing",
        "Packaging",
        "Textile"
    ]
}

# ======================================================
# Customer Locations
# ======================================================

CUSTOMER_LOCATIONS = {

    "NCR": [
        ("Quezon City", "Metro Manila"),
        ("Makati", "Metro Manila"),
        ("Pasig", "Metro Manila"),
        ("Taguig", "Metro Manila"),
        ("Manila", "Metro Manila")
    ],

    "CALABARZON": [
        ("Santa Rosa", "Laguna"),
        ("Calamba", "Laguna"),
        ("Biñan", "Laguna"),
        ("San Pablo", "Laguna"),
        ("Lipa", "Batangas"),
        ("Dasmariñas", "Cavite"),
        ("Antipolo", "Rizal")
    ],

    "Central Luzon": [
        ("Angeles", "Pampanga"),
        ("San Fernando", "Pampanga"),
        ("Tarlac City", "Tarlac"),
        ("Malolos", "Bulacan"),
        ("Balanga", "Bataan")
    ],

    "Central Visayas": [
        ("Cebu City", "Cebu"),
        ("Mandaue", "Cebu"),
        ("Lapu-Lapu", "Cebu"),
        ("Tagbilaran", "Bohol")
    ],

    "Western Visayas": [
        ("Iloilo City", "Iloilo"),
        ("Bacolod", "Negros Occidental"),
        ("Roxas", "Capiz")
    ],

    "Davao Region": [
        ("Davao City", "Davao del Sur"),
        ("Tagum", "Davao del Norte"),
        ("Panabo", "Davao del Norte")
    ],

    "Northern Mindanao": [
        ("Cagayan de Oro", "Misamis Oriental"),
        ("Iligan", "Lanao del Norte")
    ]

}

REGION_DISTRIBUTION = {

    "NCR": 30,

    "CALABARZON": 20,

    "Central Luzon": 20,

    "Central Visayas": 10,

    "Western Visayas": 7,

    "Davao Region": 8,

    "Northern Mindanao": 5

}

# ======================================================
# Customer Company Name Components
# ======================================================

COMPANY_DESCRIPTORS = [

    "North",
    "South",
    "East",
    "West",

    "Blue",
    "Silver",
    "Golden",
    "Green",
    "Red",
    "Black",

    "Prime",
    "Grand",
    "Urban",
    "True",
    "Bright",
    "Clear",

    "Pioneer",
    "Legacy",
    "Frontier",
    "Unity",

    "Summerset",
    "Ever",
    "Solid",
    "First",
    "Core"

]

COMPANY_CORES = [

    "Bridge",
    "Peak",
    "Point",
    "Harbor",
    "Gate",

    "Vision",
    "River",
    "Stone",
    "Forge",
    "Field",

    "Works",
    "Crest",
    "Horizon",
    "Line",
    "Edge",

    "Axis",
    "Link",
    "Hill",
    "Wood",
    "Vista",

    "Reach",
    "Center",
    "Valley",
    "Trail",
    "Anchor"

]



COMPANY_SUFFIXES = {

    "Corporate": [
        "Technologies Inc.",
        "Business Solutions",
        "Consulting Group",
        "Holdings Corporation"
    ],

    "Retail Business": [
        "Retail Group",
        "Trading Corporation",
        "Commercial Center"
    ],

    "Education": [
        "University",
        "State College",
        "Academy",
        "Learning Institute"
    ],

    "Government": [
        "City Government",
        "Municipal Government",
        "Public Service Office"
    ],

    "Healthcare": [
        "Medical Center",
        "General Hospital",
        "Diagnostic Clinic"
    ],

    "Manufacturing": [
        "Manufacturing Corporation",
        "Industrial Corporation",
        "Packaging Industries"
    ]
}

CUSTOMER_CREDIT_LIMITS = {

    "Corporate": (300000, 2000000),

    "Retail Business": (50000, 250000),

    "Education": (150000, 800000),

    "Government": (500000, 3000000),

    "Healthcare": (300000, 1500000),

    "Manufacturing": (500000, 2500000)

}

CUSTOMER_PAYMENT_TERMS = {

    "Corporate": [
        "Net 30",
        "Net 45",
        "Net 60"
    ],

    "Retail Business": [
        "Net 15",
        "Net 30"
    ],

    "Education": [
        "Net 30",
        "Net 60"
    ],

    "Government": [
        "Net 60"
    ],

    "Healthcare": [
        "Net 30",
        "Net 45"
    ],

    "Manufacturing": [
        "Net 30",
        "Net 45",
        "Net 60"
    ]

}

# ======================================================
# Customer Account Assignment Rules
# ======================================================

ACCOUNT_ASSIGNMENT_WEIGHTS = {

    "High": {

        "tiers": [
            "Top",
            "Middle"
        ],

        "weights": [
            85,
            15
        ]

    },

    "Medium": {

        "tiers": [
            "Middle",
            "Top",
            "New"
        ],

        "weights": [
            70,
            20,
            10
        ]

    },

    "Low": {

        "tiers": [
            "New",
            "Middle"
        ],

        "weights": [
            80,
            20
        ]

    }

}

# ======================================================
# Employee Configuration
# ======================================================

TOTAL_EMPLOYEES = 30

EMPLOYEE_DEPARTMENTS = {

    "Executive": 1,

    "Warehouse": 10,

    "Sales": 8,

    "Procurement": 3,

    "Finance": 3,

    "Human Resources": 2,

    "IT": 2,

    "Operations": 1

}

# ======================================================
# Department Job Structure
# ======================================================

EMPLOYEE_POSITIONS = {

    "Executive": [

        "General Manager"

    ],

    "Sales": [

        "Sales Manager",

        "Sales Representative"

    ],

    "Warehouse": [

        "Warehouse Manager",

        "Warehouse Supervisor",

        "Warehouse Associate"

    ],

    "Procurement": [

        "Procurement Manager",

        "Purchasing Officer"

    ],

    "Finance": [

        "Finance Manager",

        "Accountant"

    ],

    "Human Resources": [

        "HR Manager",

        "HR Officer"

    ],

    "IT": [

        "IT Manager",

        "IT Support Specialist"

    ],

    "Operations": [

        "Operations Manager"

    ]

}

# ======================================================
# Employment Types
# ======================================================

EMPLOYMENT_TYPES = {

    "Regular": 80,

    "Probationary": 15,

    "Contract": 5

}

# ======================================================
# Employee Status
# ======================================================

EMPLOYEE_STATUS = {

    "Active": 92,

    "On Leave": 5,

    "Resigned": 3

}

# ======================================================
# Monthly Salary Ranges (PHP)
# ======================================================

SALARY_RANGES = {

    "General Manager": (120000, 180000),

    "Sales Manager": (70000, 100000),

    "Sales Representative": (25000, 40000),

    "Warehouse Manager": (70000, 95000),

    "Warehouse Supervisor": (45000, 60000),

    "Warehouse Associate": (20000, 30000),

    "Procurement Manager": (70000, 95000),

    "Purchasing Officer": (30000, 45000),

    "Finance Manager": (70000, 100000),

    "Accountant": (35000, 55000),

    "HR Manager": (70000, 95000),

    "HR Officer": (28000, 40000),

    "IT Manager": (75000, 100000),

    "IT Support Specialist": (35000, 50000),

    "Operations Manager": (70000, 95000)

}

# ======================================================
# Employee Hire Date Ranges
# ======================================================


HIRE_DATE_RANGES = {

    "General Manager": (
        pd.to_datetime("2021/1/1").date(),
        pd.to_datetime("2021/3/31").date()
    ),

    "Sales Manager": (
        pd.to_datetime("2021/3/1").date(),
        pd.to_datetime("2022/12/31").date()
    ),

    "Warehouse Manager": (
        pd.to_datetime("2021/3/1").date(),
        pd.to_datetime("2022/12/31").date()
    ),

    "Procurement Manager": (
        pd.to_datetime("2021/3/1").date(),
        pd.to_datetime("2022/12/31").date()
    ),

    "Finance Manager": (
        pd.to_datetime("2021/3/1").date(),
        pd.to_datetime("2022/12/31").date()
    ),

    "HR Manager": (
        pd.to_datetime("2021/3/1").date(),
        pd.to_datetime("2022/12/31").date()
    ),

    "IT Manager": (
        pd.to_datetime("2021/3/1").date(),
        pd.to_datetime("2022/12/31").date()
    ),

    "Operations Manager": (
        pd.to_datetime("2021/3/1").date(),
        pd.to_datetime("2022/12/31").date()
    ),

    "Warehouse Supervisor": (
        pd.to_datetime("2021/6/1").date(),
        pd.to_datetime("2023/12/31").date()
    ),

    "Sales Representative": (
        pd.to_datetime("2021/6/1").date(),
        TODAY
    ),

    "Warehouse Associate": (
        pd.to_datetime("2021/6/1").date(),
        TODAY
    ),

    "Purchasing Officer": (
        pd.to_datetime("2021/6/1").date(),
        TODAY
    ),

    "Accountant": (
        pd.to_datetime("2021/6/1").date(),
        TODAY
    ),

    "HR Officer": (
        pd.to_datetime("2021/6/1").date(),
        TODAY
    ),

    "IT Support Specialist": (
        pd.to_datetime("2021/6/1").date(),
        TODAY
    )

}

ORDER_PRODUCT_COUNT = {

    1: 40,
    2: 30,
    3: 15,
    4: 8,
    5: 4,
    6: 2,
    7: 0.8,
    8: 0.2

}

CATEGORY_ORDER_WEIGHT = {

        "Accessories": 22,

        "Storage": 18,

        "Networking": 15,

        "Laptop": 12,

        "Desktop": 10,

        "Printer": 8,

        "Monitor": 7,

        "Office Equipment": 5

    }

ORDER_QUANTITY = {

    1: 35,
    2: 25,
    3: 15,
    4: 10,
    5: 6,
    6: 4,
    7: 2,
    8: 1.5,
    9: 1,
    10: 0.5

}

DISCOUNT_PERCENTAGES = {

    0.00: 45,

    0.05: 25,

    0.10: 18,

    0.15: 8,

    0.20: 3,

    0.25: 1

}

WAREHOUSES = [

    {
        "warehouse_id": "WH001",
        "warehouse_name": "North Distribution Center",
        "region": "North Luzon"
    },

    {
        "warehouse_id": "WH002",
        "warehouse_name": "Central Distribution Center",
        "region": "Metro Manila"
    },

    {
        "warehouse_id": "WH003",
        "warehouse_name": "South Distribution Center",
        "region": "South Luzon"
    }

]

# ======================================================
# Warehouse Product Assignment
# ======================================================

WAREHOUSE_PRODUCT_MAP = {

    "North Distribution Center": [

        "Printer",
        "Monitor"

    ],

    "Central Distribution Center": [

        "Networking",
        "Office Equipment"

    ],

    "South Distribution Center": [

        "Laptop",
        "Desktop",
        "Storage",
        "Accessories"

    ]

}

# ======================================================
# Inventory Coverage Configuration
# ======================================================

INVENTORY_MONTHS = 30

FAST_MOVING_MONTHS = {

    1.0: 15,
    1.5: 35,
    2.0: 35,
    2.5: 15

}

MEDIUM_MOVING_MONTHS = {

    2.0: 20,
    2.5: 35,
    3.0: 30,
    4.0: 15

}

SLOW_MOVING_MONTHS = {

    4.0: 25,
    5.0: 45,
    6.0: 30

}

RESERVED_STOCK_PERCENTAGES = {

    0.00: 20,
    0.05: 35,
    0.10: 30,
    0.15: 15

}

# ------------------------------------------------------
# Utility Functions
# ------------------------------------------------------

def save_csv(df: pd.DataFrame, filename: str):

    filepath = RAW_DIR / filename

    df.to_csv(
        filepath,
        index=False,
        encoding="utf-8-sig"
    )

    print("✓ Saved")

def generate_mobile():

    prefix = random.choice(PH_MOBILE_PREFIXES)

    suffix = "".join(
        random.choice("0123456789")
        for _ in range(7)
    )

    return prefix + suffix


# ------------------------------------------------------
# Email Generator
# ------------------------------------------------------

def email_from_contact(first_name, last_name, domain):

    first = first_name.lower()

    last = last_name.lower()

    first = re.sub(r"[^a-z]", "", first)

    last = re.sub(r"[^a-z]", "", last)

    return f"{first}.{last}@{domain}.com"

# ======================================================
# Generate Record Timestamps
# ======================================================

def generate_record_timestamps(reference_date):
    """
    Generates realistic created_at and updated_at timestamps.

    Rules

    - created_at is on or shortly after the business event
    - updated_at is always >= created_at
    """

    created_at = fake.date_time_between(

        start_date=reference_date,

        end_date=min(
            reference_date + pd.Timedelta(days=7),
            TODAY
        )

    )

    updated_at = fake.date_time_between(

        start_date=created_at,

        end_date=TODAY

    )

    return created_at, updated_at

# ======================================================
# Generate Employee Hire Date
# ======================================================

def generate_hire_date(job_title):
    """
    Generates a realistic hire date
    based on the employee's position.
    """

    start_date, end_date = HIRE_DATE_RANGES[job_title]

    total_days = (
        end_date - start_date
    ).days

    hire_date = start_date + pd.Timedelta(
        days=random.randint(
            0,
            total_days
        )
    )

    return hire_date

# ======================================================
# Generate Employee Salary
# ======================================================

def generate_salary(job_title):
    """
    Generates a realistic monthly salary
    based on the employee's position.

    Salaries are rounded to the nearest
    PHP 500.
    """

    minimum, maximum = SALARY_RANGES[
        job_title
    ]

    salary = random.randint(
        minimum,
        maximum
    )

    salary = (
        round(salary / 500) * 500
    )

    return salary

# ======================================================
# Build Employee Record
# ======================================================

def build_employee_record(
    blueprint_entry,
    manager_lookup,
    supplier_reference,
    customer_reference,
    employee_state
):
    """
    Builds one complete employee record
    from a blueprint entry.
    """

    # ------------------------------------------
    # Employee Name
    # ------------------------------------------

    name = generate_employee_name(
        employee_state
    )

    # ------------------------------------------
    # Manager ID
    # ------------------------------------------

    manager_position = blueprint_entry[
        "manager_position"
    ]

    if manager_position is None:

        manager_id = ""

    else:

        manager_id = manager_lookup[
            manager_position
        ]

    # ------------------------------------------
    # Hire Date & Record Timestamps
    # ------------------------------------------

    hire_date = generate_hire_date(
        blueprint_entry["job_title"]
    )

    created_at, updated_at = (
        generate_record_timestamps(
            hire_date
        )
    )

    # ------------------------------------------
    # Build Record
    # ------------------------------------------

    employee = {

        "employee_id":
            blueprint_entry["employee_id"],

        "first_name":
            name["first_name"],

        "last_name":
            name["last_name"],

        "full_name":
            name["full_name"],

        "department":
            blueprint_entry["department"],

        "job_title":
            blueprint_entry["job_title"],

        "manager_id":
            manager_id,

        "email":
            generate_employee_email(
                name["full_name"],
                employee_state
            ),

        "mobile_number":
            generate_employee_mobile(
                supplier_reference,
                customer_reference,
                employee_state
            ),

        "hire_date":
            hire_date,

        "employment_type":
            random.choices(
                list(
                    EMPLOYMENT_TYPES.keys()
                ),
                weights=list(
                    EMPLOYMENT_TYPES.values()
                ),
                k=1
            )[0],

        "salary":
            generate_salary(
                blueprint_entry["job_title"]
            ),

        "status":
            random.choices(
                list(
                    EMPLOYEE_STATUS.keys()
                ),
                weights=list(
                    EMPLOYEE_STATUS.values()
                ),
                k=1
            )[0],

        "created_at":
            created_at,

        "updated_at":
            updated_at

    }

    return employee

# ======================================================
# Generate Employees
# ======================================================

def generate_employees():

    print("Generating employees...")

    supplier_reference = (
        load_supplier_reference_data()
    )

    customer_reference = (
        load_customer_reference_data()
    )

    employee_state = (
        create_employee_state()
    )

    blueprint = (
        build_employee_blueprint()
    )

    blueprint = (
        assign_employee_ids(
            blueprint
        )
    )

    manager_lookup = (
        build_manager_lookup(
            blueprint
        )
    )

    employees = []

    for blueprint_entry in blueprint:

        employee = build_employee_record(

            blueprint_entry,

            manager_lookup,

            supplier_reference,

            customer_reference,

            employee_state

        )

        employees.append(
            employee
        )

    employees_df = pd.DataFrame(
        employees
    )

    employee_file = (
        RAW_DIR / "employees.csv"
    )

    employees_df.to_csv(

        employee_file,

        index=False

    )

    validate_employees(
        employees_df
    )

    print(
        f"✓ {len(employees_df)} employees generated."
    )

    print(
        "✓ employees.csv saved."
    )

    return employees_df

# ======================================================
# Employee Validation
# ======================================================

def validate_employees(employees_df):

    print()

    print("Running employee validations...")

    # --------------------------------------------------
    # Employee ID
    # --------------------------------------------------

    assert employees_df["employee_id"].is_unique

    print("✓ Employee IDs are unique")

    # --------------------------------------------------
    # Full Name
    # --------------------------------------------------

    assert employees_df["full_name"].is_unique

    print("✓ Employee names are unique")

    # --------------------------------------------------
    # Email
    # --------------------------------------------------

    assert employees_df["email"].is_unique

    print("✓ Employee emails are unique")

    # --------------------------------------------------
    # Mobile
    # --------------------------------------------------

    assert employees_df["mobile_number"].is_unique

    print("✓ Employee mobile numbers are unique")

    # --------------------------------------------------
    # Manager Validation
    # --------------------------------------------------

    employee_ids = set(
        employees_df["employee_id"]
    )

    for manager_id in employees_df["manager_id"]:

        if manager_id == "":

            continue

        assert manager_id in employee_ids

    print("✓ Manager hierarchy validated")

    # --------------------------------------------------
    # Department Validation
    # --------------------------------------------------

    valid_departments = set(
        EMPLOYEE_DEPARTMENTS.keys()
    )

    assert set(
        employees_df["department"]
    ).issubset(
        valid_departments
    )

    print("✓ Departments validated")

    # --------------------------------------------------
    # Department Headcount Validation
    # --------------------------------------------------

    department_counts = (
        employees_df["department"]
        .value_counts()
        .to_dict()
    )

    for department, expected_count in (
        EMPLOYEE_DEPARTMENTS.items()
    ):

        actual_count = department_counts.get(
            department,
            0
        )

        assert (
            actual_count == expected_count
        ), (

            f"{department}: "

            f"expected {expected_count}, "

            f"found {actual_count}"

        )

    print("✓ Department headcount validated")
    
    # --------------------------------------------------
    # Job Titles
    # --------------------------------------------------

    valid_titles = set()

    for titles in EMPLOYEE_POSITIONS.values():

        valid_titles.update(
            titles
        )

    assert set(
        employees_df["job_title"]
    ).issubset(
        valid_titles
    )

    print("✓ Job titles validated")

    # --------------------------------------------------
    # Salary Validation
    # --------------------------------------------------

    for _, employee in employees_df.iterrows():

        minimum, maximum = SALARY_RANGES[
            employee["job_title"]
        ]

        assert (

            minimum

            <= employee["salary"]

            <= maximum

        )

    print("✓ Salary ranges validated")

    # --------------------------------------------------
    # Hire Dates
    # --------------------------------------------------

    for _, employee in employees_df.iterrows():

        hire_date = pd.to_datetime(
            employee["hire_date"]
        ).date()

        start_date, end_date = HIRE_DATE_RANGES[
            employee["job_title"]
        ]

        assert (

            start_date

            <= hire_date

            <= end_date

        )

    print("✓ Hire dates validated")

    # --------------------------------------------------
    # Employment Type
    # --------------------------------------------------

    assert set(

        employees_df[
            "employment_type"
        ]

    ).issubset(

        EMPLOYMENT_TYPES.keys()

    )

    print("✓ Employment types validated")

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    assert set(

        employees_df[
            "status"
        ]

    ).issubset(

        EMPLOYEE_STATUS.keys()

    )

    print("✓ Employee status validated")

    # --------------------------------------------------
    # Timestamp Validation
    # --------------------------------------------------

    created = pd.to_datetime(
        employees_df["created_at"]
    )

    updated = pd.to_datetime(
        employees_df["updated_at"]
    )

    assert (

        created <= updated

    ).all()

    print("✓ Timestamp validation passed")

    print()

    print(
        "ALL EMPLOYEE VALIDATIONS PASSED"
    )

    print()

# ======================================================
# Employee State
# ======================================================

def create_employee_state():
    """
    Stores generated employee information
    to prevent duplicates.
    """

    return {

        "used_employee_ids": set(),

        "used_full_names": set(),

        "used_emails": set(),

        "used_mobiles": set()

    }

# ======================================================
# Generate Employee Name
# ======================================================

def generate_employee_name(employee_state):
    """
    Generates a unique Filipino employee name.
    """

    while True:

        first_name = random.choice(
            FILIPINO_FIRST_NAMES
        )

        last_name = random.choice(
            FILIPINO_LAST_NAMES
        )

        full_name = (
            f"{first_name} {last_name}"
        )

        if full_name not in employee_state["used_full_names"]:

            employee_state["used_full_names"].add(
                full_name
            )

            return {

                "first_name": first_name,

                "last_name": last_name,

                "full_name": full_name

            }

# ======================================================
# Build Manager Lookup
# ======================================================

def build_manager_lookup(blueprint):
    """
    Builds a lookup table that maps
    job titles to employee IDs.

    Example:

    {
        "General Manager": "EMP0001",
        "Sales Manager": "EMP0002"
    }
    """

    lookup = {}

    for employee in blueprint:

        lookup[
            employee["job_title"]
        ] = employee["employee_id"]

    return lookup

# ======================================================
# Employee ID Generator
# ======================================================

def generate_employee_id(number):

    return f"EMP{number:04d}"

# ======================================================
# Generate Order ID
# ======================================================

def generate_order_id(
    sequence
):
    """
    Generates sequential order IDs.
    """

    return f"ORD{sequence:06d}"

# ======================================================
# Build Employee Organization Blueprint
# ======================================================

def build_employee_blueprint():
    """
    Creates the LOTS Corp organizational structure.

    Returns:
        List[dict]
    """

    blueprint = []

    # ----------------------------------------------
    # Executive
    # ----------------------------------------------

    blueprint.append({

        "department": "Executive",

        "job_title": "General Manager",

        "manager_position": None,

        "position_order": 1

    })

    # ----------------------------------------------
    # Sales
    # ----------------------------------------------

    blueprint.append({

        "department": "Sales",

        "job_title": "Sales Manager",

        "manager_position": "General Manager",

        "position_order": 2

    })

    for _ in range(7):

        blueprint.append({

            "department": "Sales",

            "job_title": "Sales Representative",

            "manager_position": "Sales Manager",

            "position_order": 4

        })

    # ----------------------------------------------
    # Warehouse
    # ----------------------------------------------

    blueprint.append({

        "department": "Warehouse",

        "job_title": "Warehouse Manager",

        "manager_position": "General Manager",

        "position_order": 2

    })

    blueprint.append({

        "department": "Warehouse",

        "job_title": "Warehouse Supervisor",

        "manager_position": "Warehouse Manager",

        "position_order": 3

    })

    for _ in range(8):

        blueprint.append({

            "department": "Warehouse",

            "job_title": "Warehouse Associate",

            "manager_position": "Warehouse Supervisor",

            "position_order": 4

        })

    # ----------------------------------------------
    # Procurement
    # ----------------------------------------------

    blueprint.append({

        "department": "Procurement",

        "job_title": "Procurement Manager",

        "manager_position": "General Manager",

        "position_order": 2

    })

    for _ in range(2):

        blueprint.append({

            "department": "Procurement",

            "job_title": "Purchasing Officer",

            "manager_position": "Procurement Manager",

            "position_order": 4

        })

    # ----------------------------------------------
    # Finance
    # ----------------------------------------------

    blueprint.append({

        "department": "Finance",

        "job_title": "Finance Manager",

        "manager_position": "General Manager",

        "position_order": 2

    })

    for _ in range(2):

        blueprint.append({

            "department": "Finance",

            "job_title": "Accountant",

            "manager_position": "Finance Manager",

            "position_order": 4

        })

    # ----------------------------------------------
    # Human Resources
    # ----------------------------------------------

    blueprint.append({

        "department": "Human Resources",

        "job_title": "HR Manager",

        "manager_position": "General Manager",

        "position_order": 2

    })

    blueprint.append({

        "department": "Human Resources",

        "job_title": "HR Officer",

        "manager_position": "HR Manager",

        "position_order": 4

    })

    # ----------------------------------------------
    # IT
    # ----------------------------------------------

    blueprint.append({

        "department": "IT",

        "job_title": "IT Manager",

        "manager_position": "General Manager",

        "position_order": 2

    })

    blueprint.append({

        "department": "IT",

        "job_title": "IT Support Specialist",

        "manager_position": "IT Manager",

        "position_order": 4

    })

    # ----------------------------------------------
    # Operations
    # ----------------------------------------------

    blueprint.append({

        "department": "Operations",

        "job_title": "Operations Manager",

        "manager_position": "General Manager",

        "position_order": 2

    })

    assert len(blueprint) == TOTAL_EMPLOYEES

    return blueprint

# ======================================================
# Assign Employee IDs to Blueprint
# ======================================================

def assign_employee_ids(blueprint):
    """
    Assigns sequential employee IDs to every
    blueprint entry.

    Returns the updated blueprint.
    """

    for index, employee in enumerate(
        blueprint,
        start=1
    ):

        employee["employee_id"] = generate_employee_id(
            index
        )

    return blueprint

# ======================================================
# Name Slug Helper
# ======================================================

def slugify_name(text):
    """
    Converts a person's name into an email-friendly slug.

    Example:

    Juan Dela Cruz

    becomes

    juan.delacruz
    """

    text = text.lower().strip()

    replacements = {

        " dela ": " delacruz_temp ",
        " de ": " de",
        " del ": " del",
        " la ": "",
        " ": ".",
        "'": "",
        "-": ""

    }

    for old, new in replacements.items():

        text = text.replace(old, new)

    text = text.replace(
        "delacruz_temp",
        "delacruz"
    )

    return text

# ======================================================
# Employee Email Generator
# ======================================================

def generate_employee_email(
    full_name,
    employee_state
):
    """
    Generates a unique LOTS Corp employee email.
    """

    while True:

        username = slugify_name(
            full_name
        )

        email = (
            f"{username}@lotscorp.com"
        )

        if email not in employee_state["used_emails"]:

            employee_state["used_emails"].add(
                email
            )

            return email

        username = (
            f"{username}{random.randint(1,99)}"
        )

# ======================================================
# Employee Mobile Generator
# ======================================================

def generate_employee_mobile(
    supplier_reference,
    customer_reference,
    employee_state
):
    """
    Generates a unique Philippine mobile number.

    The number must not exist in:

    - Suppliers
    - Customers
    - Employees
    """

    while True:

        prefix = random.choice(
            PH_MOBILE_PREFIXES
        )

        number = (
            prefix
            +
            fake.numerify("#######")
        )

        if (

            number not in supplier_reference["mobiles"]

            and

            number not in customer_reference["mobiles"]

            and

            number not in employee_state["used_mobiles"]

        ):

            employee_state["used_mobiles"].add(
                number
            )

            return number

# ------------------------------------------------------
# Supplier Generator
# ------------------------------------------------------

def generate_suppliers():

    rows = []
    used_contacts = set()

    for i, (supplier_name, domain) in enumerate(SUPPLIERS, start=1):

        # ---------- Unique Contact Person ----------
        while True:
            first_name = random.choice(FIRST_NAMES)
            last_name = random.choice(LAST_NAMES)

            full_name = f"{first_name} {last_name}"

            if full_name not in used_contacts:
                used_contacts.add(full_name)
                break

        # ---------- Location ----------
        region, province, city = random.choice(LOCATIONS)

        # ---------- Dates ----------
        created_at = (
            pd.Timestamp("2021-01-01")
            + pd.to_timedelta(random.randint(0, 900), unit="D")
        )

        updated_at = (
            created_at
            + pd.to_timedelta(random.randint(30, 700), unit="D")
        )

        # Prevent future dates
        today = pd.Timestamp.today().normalize()

        if updated_at > today:
            updated_at = today

        # ---------- Supplier Record ----------
        rows.append({

            "supplier_id":
                f"SUP{i:04d}",

            "supplier_name":
                supplier_name,

            "contact_person":
                full_name,

            "email":
                email_from_contact(
                    first_name,
                    last_name,
                    domain
                ),

            "mobile_number":
                generate_mobile(),

            "street_address":
                f"{random.randint(10,999)} Business Park",

            "city":
                city,

            "province":
                province,

            "region":
                region,

            "country":
                "Philippines",

            "payment_terms":
                random.choice(PAYMENT_TERMS),

            "lead_time_days":
                random.randint(3, 30),

            "supplier_status":
                random.choices(
                    SUPPLIER_STATUS,
                    weights=[90, 10],
                    k=1
                )[0],

            "created_at":
                created_at.date(),

            "updated_at":
                updated_at.date()

        })

    return pd.DataFrame(rows)

# ======================================================
# PRODUCT CATALOG SUMMARY
# ======================================================

def summarize_product_catalog():

    print("\nProduct Catalog Summary")
    print("-" * 40)

    total_products = 0

    category_totals = {}

    for family in PRODUCT_FAMILIES:

        category = family["category"]

        count = len(family["variants"])

        category_totals[category] = (
            category_totals.get(category, 0)
            + count
        )

        total_products += count

    for category, count in sorted(category_totals.items()):

        print(f"{category:<20} {count:>3}")

    print("-" * 40)

    print(f"{'TOTAL PRODUCTS':<20} {total_products:>3}")

    print()

# ======================================================
# Load Supplier Reference Data
# ======================================================

def load_supplier_reference_data():
    """
    Loads supplier master data and returns sets used to
    prevent duplicate customer information.
    """

    supplier_file = RAW_DIR / "suppliers.csv"

    if not supplier_file.exists():
        raise FileNotFoundError(
            f"Supplier file not found: {supplier_file}"
        )

    suppliers_df = pd.read_csv(supplier_file)

    required_columns = [
    "supplier_name",
    "contact_person",
    "mobile_number",
    "email"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in suppliers_df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"suppliers.csv is missing required columns: {missing_columns}"
        )

    supplier_names = set(
        suppliers_df["supplier_name"].str.strip()
    )

    supplier_contacts = set(
        suppliers_df["contact_person"].str.strip()
    )

    supplier_mobiles = set(
        suppliers_df["mobile_number"].astype(str).str.strip()
    )

    supplier_emails = set(
        suppliers_df["email"].str.lower().str.strip()
    )

    supplier_domains = set(
        suppliers_df["email"]
        .str.lower()
        .str.split("@")
        .str[-1]
        .str.strip()
    )

    return {

        "names": supplier_names,

        "contacts": supplier_contacts,

        "mobiles": supplier_mobiles,

        "emails": supplier_emails,

        "domains": supplier_domains

    }

# ======================================================
# Load Customer Reference Data
# ======================================================

def load_customer_reference_data():
    """
    Loads customer master data to prevent
    duplicate employee contact information.
    """

    customer_file = RAW_DIR / "customers.csv"

    if not customer_file.exists():

        raise FileNotFoundError(
            f"Customer file not found: {customer_file}"
        )

    customers_df = pd.read_csv(
        customer_file
    )

    return {

        "mobiles": set(
            customers_df["mobile_number"]
            .astype(str)
            .str.strip()
        ),

        "emails": set(
            customers_df["email"]
            .str.lower()
            .str.strip()
        ),

        "contacts": set(
            customers_df["contact_person"]
            .str.strip()
        )

    }

# ======================================================
# Load Order Reference Data
# ======================================================

def load_order_reference_data():
    """
    Loads master data required for order generation.
    Only active records eligible for new orders are returned.
    """

    customers_df = pd.read_csv(
        RAW_DIR / "customers.csv"
    )

    employees_df = pd.read_csv(
        RAW_DIR / "employees.csv"
    )

    products_df = pd.read_csv(
        RAW_DIR / "products.csv"
    )

    # ------------------------------------------
    # Active Customers
    # ------------------------------------------

    active_customers = customers_df[
        customers_df["status"] == "Active"
    ].copy()

    active_customers = assign_customer_activity(
        active_customers
    )

    active_customers = assign_order_capacity(
        active_customers
    )

    active_customers = normalize_order_capacity(
        active_customers
    )

    print()
    print("=" * 60)
    print("Customer Activity Summary")
    print("=" * 60)

    print(
        active_customers[
            "activity_level"
        ].value_counts()
    )

    print()

    print(
        active_customers.groupby(
            "activity_level"
        )["order_capacity"].sum()
    )

    print()

    print(
        "Total Planned Orders:",
        active_customers[
            "order_capacity"
        ].sum()
    )

    # ------------------------------------------
    # Active Sales Representatives
    # ------------------------------------------

    active_sales_reps = employees_df[
        (employees_df["status"] == "Active")
        &
        (
            employees_df["job_title"]
            == "Sales Representative"
        )
    ].copy()

    active_customers = (
        assign_customer_account_managers(
            active_customers,
            active_sales_reps
        )
    )

    # ------------------------------------------
    # Active Products
    # ------------------------------------------

    active_products = products_df[
        products_df["active"] == True
    ].copy()

    return {

        "customers": active_customers,

        "sales_reps": active_sales_reps,

        "products": active_products

    }

def load_order_details_reference_data():
    """
    Loads reference data required for
    generating Order Details.

    Only completed Orders are loaded.

    Only active Products are eligible
    for new Order Detail records.
    """

    # ------------------------------------------
    # Orders
    # ------------------------------------------

    orders_df = pd.read_csv(
        RAW_DIR / "orders.csv",
        parse_dates=[
            "order_date",
            "created_at",
            "updated_at"
        ]
    )

    # ------------------------------------------
    # Products
    # ------------------------------------------

    products_df = pd.read_csv(
        RAW_DIR / "products.csv",
        parse_dates=[
            "launch_date",
            "created_at",
            "updated_at"
        ]
    )

    # ------------------------------------------
    # Active Products
    # ------------------------------------------

    active_products = products_df[
        products_df["active"] == True
    ].copy()

    print()

    print("=" * 60)
    print("Order Details Reference Data")
    print("=" * 60)

    print(
        "Orders:",
        len(orders_df)
    )

    print(
        "Active Products:",
        len(active_products)
    )

    return {

        "orders": orders_df,

        "products": active_products

    }

def load_inventory_reference_data():
    """
    Loads all reference data required
    for generating inventory.
    """

    products_df = pd.read_csv(
        RAW_DIR / "products.csv"
    )

    products_df = assign_product_warehouse(
        products_df
    )

    orders_df = pd.read_csv(
        RAW_DIR / "orders.csv"
    )

    order_details_df = pd.read_csv(
        RAW_DIR / "order_details.csv"
    )

    print()

    print("=" * 60)

    print("Inventory Reference Data")

    print("=" * 60)

    print(
        "Products:",
        len(products_df)
    )

    print(
        "Orders:",
        len(orders_df)
    )

    print(
        "Order Details:",
        len(order_details_df)
    )

    return {

        "products": products_df,

        "orders": orders_df,

        "order_details": order_details_df

    }

# ======================================================
# Initialize Order State
# ======================================================

def initialize_order_state():
    """
    Initializes state used during order generation.
    """

    return {

        "used_order_ids": set()

    }

# ======================================================
# Assign Customer Activity
# ======================================================

def assign_customer_activity(
    customers_df
):
    """
    Assigns a deterministic activity level to every
    active customer.

    Distribution always matches CUSTOMER_ACTIVITY.
    """

    customers = customers_df.copy()

    total_customers = len(customers)

    activity_labels = []

    allocated = 0

    activity_items = list(
        CUSTOMER_ACTIVITY.items()
    )

    for index, (
        activity,
        percentage
    ) in enumerate(activity_items):

        if index == len(activity_items) - 1:

            count = (
                total_customers
                - allocated
            )

        else:

            count = round(
                total_customers
                * percentage
                / 100
            )

        activity_labels.extend(
            [activity] * count
        )

        allocated += count

    random.shuffle(
        activity_labels
    )

    customers["activity_level"] = (
        activity_labels
    )

    return customers

# ======================================================
# Assign Order Capacity
# ======================================================

def assign_order_capacity(
    customers_df
):
    """
    Assigns the total number of orders each customer
    will generate.
    """

    customers = customers_df.copy()

    capacities = []

    for activity in customers[
        "activity_level"
    ]:

        minimum, maximum = (
            ORDER_FREQUENCY[
                activity
            ]
        )

        capacities.append(

            random.randint(
                minimum,
                maximum
            )

        )

    customers[
        "order_capacity"
    ] = capacities

    return customers

# ======================================================
# Normalize Order Capacity
# ======================================================

def normalize_order_capacity(
    customers_df
):
    """
    Scales customer order capacities so that the
    total equals ORDER_COUNT.
    """

    customers = customers_df.copy()

    total_capacity = customers[
        "order_capacity"
    ].sum()

    scale = (
        ORDER_COUNT
        / total_capacity
    )

    customers[
        "order_capacity"
    ] = (
        customers["order_capacity"]
        * scale
    ).round().astype(int)

    # ------------------------------------------
    # Final Correction
    # ------------------------------------------

    difference = (
        ORDER_COUNT
        - customers["order_capacity"].sum()
    )

    if difference > 0:

        while difference > 0:

            index = random.choice(
                customers.index.tolist()
            )

            customers.loc[
                index,
                "order_capacity"
            ] += 1

            difference -= 1

    elif difference < 0:

        while difference < 0:

            candidates = customers[
                customers["order_capacity"] > 1
            ]

            index = random.choice(
                candidates.index.tolist()
            )

            customers.loc[
                index,
                "order_capacity"
            ] -= 1

            difference += 1

    return customers

# ======================================================
# Initialize Customer State
# ======================================================

def initialize_customer_state():
    """
    Creates the state object used throughout
    customer generation.

    This keeps track of values that must remain
    globally unique within the Customer Master.
    """

    return {

        "used_names": set(),

        "used_contacts": set(),

        "used_domains": set(),

        "used_emails": set(),

        "used_mobiles": set(),

        "used_prefixes": set()

    }

# ======================================================
# Generate Company Prefix
# ======================================================

def generate_company_prefix(used_prefixes):

    max_attempts = 500

    for _ in range(max_attempts):

        prefix = (
            random.choice(COMPANY_DESCRIPTORS)
            +
            random.choice(COMPANY_CORES)
        )

        if prefix not in used_prefixes:

            used_prefixes.add(prefix)

            return prefix

    raise ValueError(
        "Unable to generate a unique company prefix."
    )

# ======================================================
# Generate Customer Company Name
# ======================================================

def generate_company_name(
    customer_type,
    supplier_reference,
    customer_state
):
    """
    Generates a unique fictional customer company name.
    """

    while True:

        prefix = generate_company_prefix(
            customer_state["used_prefixes"]
        )

        core = random.choice(
            COMPANY_CORES
        )

        suffix = random.choice(
            COMPANY_SUFFIXES[customer_type]
        )

        company_name = f"{prefix} {core} {suffix}"

        if (
            company_name not in supplier_reference["names"]
            and
            company_name not in customer_state["used_names"]
        ):

            customer_state["used_names"].add(
                company_name
            )

            return company_name

# ======================================================
# Generate Customer Contact Person
# ======================================================

def generate_contact_person(
    supplier_reference,
    customer_state
):
    """
    Generates a unique Filipino contact person.
    """

    while True:

        first_name = random.choice(
            FILIPINO_FIRST_NAMES
        )

        last_name = random.choice(
            FILIPINO_LAST_NAMES
        )

        contact_person = (
            f"{first_name} {last_name}"
        )

        if (
            contact_person not in supplier_reference["contacts"]
            and
            contact_person not in customer_state["used_contacts"]
        ):

            customer_state["used_contacts"].add(
                contact_person
            )

            return contact_person

# ======================================================
# Generate Company Domain
# ======================================================

def generate_company_domain(
    company_name,
    supplier_reference,
    customer_state
):
    """
    Generates a unique business domain.

    Example:

    NorthBridge Technologies Inc.
        -> northbridgetechnologies.com

    SilverLeaf Manufacturing Corporation
        -> silverleafmanufacturing.com
    """

    domain = company_name.lower()

    legal_suffixes = [

        " inc.",
        " corporation",
        " corp.",
        " ltd.",
        " llc"

    ]

    for suffix in legal_suffixes:
        domain = domain.replace(suffix, "")

    domain = (
        domain
        .replace("&", "")
        .replace(",", "")
        .replace(".", "")
        .replace("-", "")
    )

    domain = "".join(domain.split())

    domain += ".com"

    if domain in supplier_reference["domains"]:
        raise ValueError(
            f"Customer domain already exists in suppliers: {domain}"
        )

    if domain in customer_state["used_domains"]:
        raise ValueError(
            f"Duplicate customer domain: {domain}"
        )

    customer_state["used_domains"].add(
        domain
    )

    return domain

# ======================================================
# Clean Person Name
# ======================================================

def clean_person_name(name):
    """
    Converts a person's name into a format suitable
    for usernames and email addresses.

    Example:
        Juan Dela Cruz
            -> juan_dela_cruz

        Maria Anne Santos
            -> maria_anne_santos

        John Jr. Reyes
            -> john_reyes
    """

    suffixes = {

        "jr",
        "jr.",
        "sr",
        "sr.",
        "ii",
        "iii",
        "iv"

    }

    words = []

    for word in name.lower().split():

        cleaned = (
            word
            .replace(".", "")
            .replace(",", "")
            .replace("'", "")
            .replace("-", "")
        )

        if cleaned not in suffixes:
            words.append(cleaned)

    return "_".join(words)

# ======================================================
# Generate Customer Email
# ======================================================

def generate_customer_email(
    contact_person,
    company_domain,
    supplier_reference,
    customer_state
):
    """
    Generates a professional business email.

    Rules
    -----
    - Uses contact person's name
    - Uses company domain
    - Never duplicates supplier emails
    - Never duplicates customer emails
    """

    name = clean_person_name(contact_person)

    email = f"{name}@{company_domain}"

    if email in supplier_reference["emails"]:
        raise ValueError(
            f"Supplier email already exists: {email}"
        )

    if email in customer_state["used_emails"]:
        raise ValueError(
            f"Duplicate customer email: {email}"
        )

    customer_state["used_emails"].add(email)

    return email

# ======================================================
# Generate Customer Mobile Number
# ======================================================

def generate_customer_mobile(
    supplier_reference,
    customer_state
):
    """
    Generates a unique Philippine mobile number.

    Rules
    -----
    - Philippine format
    - Unique across suppliers
    - Unique across customers
    """

    while True:

        prefix = random.choice(
            PH_MOBILE_PREFIXES
        )

        mobile = (
            prefix
            +
            fake.numerify("#######")
        )

        if (
            mobile not in supplier_reference["mobiles"]
            and
            mobile not in customer_state["used_mobiles"]
        ):

            customer_state["used_mobiles"].add(
                mobile
            )

            return mobile

# ======================================================
# Generate Customer Classification
# ======================================================

def generate_customer_classification():
    """
    Generates a customer type and a matching industry.
    """

    customer_types = list(CUSTOMER_TYPES.keys())

    weights = list(CUSTOMER_TYPES.values())

    customer_type = random.choices(
        customer_types,
        weights=weights,
        k=1
    )[0]

    industry = random.choice(
        INDUSTRIES[customer_type]
    )

    return customer_type, industry

# ======================================================
# Generate Customer Location
# ======================================================

def generate_customer_location():
    """
    Generates a customer location based on
    realistic Philippine regional distribution.
    """

    regions = list(REGION_DISTRIBUTION.keys())

    weights = list(REGION_DISTRIBUTION.values())

    region = random.choices(
        regions,
        weights=weights,
        k=1
    )[0]

    city, province = random.choice(
        CUSTOMER_LOCATIONS[region]
    )

    return city, province, region

# ======================================================
# Generate Customer Credit Limit
# ======================================================

def generate_credit_limit(customer_type):
    """
    Generates a realistic credit limit based on
    customer type.
    """

    minimum, maximum = CUSTOMER_CREDIT_LIMITS[
        customer_type
    ]

    credit_limit = random.randint(
        minimum,
        maximum
    )

    # Round to nearest 5,000 pesos
    credit_limit = round(
        credit_limit / 5000
    ) * 5000

    return credit_limit

# ======================================================
# Generate Customer Payment Terms
# ======================================================

def generate_customer_payment_terms(customer_type):
    """
    Selects payment terms based on customer type.
    """

    return random.choice(
        CUSTOMER_PAYMENT_TERMS[
            customer_type
        ]
    )

# ======================================================
# Generate Customer Status
# ======================================================

def generate_customer_status():
    """
    Generates customer status.

    Distribution:
        Active   : 95%
        Inactive : 5%
    """

    return random.choices(

        ["Active", "Inactive"],

        weights=[95, 5],

        k=1

    )[0]

# ======================================================
# Assign Customer Account Managers
# ======================================================

def assign_customer_account_managers(
    customers_df,
    sales_reps_df
):
    """
    Assign one primary Sales Representative
    to every active customer.

    Assignment rules:

    - Customers are sorted by activity level
      and order capacity.

    - Sales Representatives are grouped by
      experience using hire date.

    - High activity customers are assigned
      to the most experienced representatives.

    - Medium activity customers are assigned
      to mid-level representatives.

    - Low activity customers are assigned
      to newer representatives.

    - Customers are distributed using
      round-robin within each experience tier.
    """

    customers = customers_df.copy()

    # ------------------------------------------
    # Sort Customers
    # ------------------------------------------

    activity_order = {
        "High": 0,
        "Medium": 1,
        "Low": 2
    }

    customers["_activity_rank"] = (
        customers["activity_level"]
        .map(activity_order)
    )

    customers = (
        customers
        .sort_values(
            by=[
                "_activity_rank",
                "order_capacity"
            ],
            ascending=[
                True,
                False
            ]
        )
        .reset_index(drop=True)
    )

    # ------------------------------------------
    # Sort Sales Representatives
    # ------------------------------------------

    sales_reps = (
        sales_reps_df
        .sort_values(
            by="hire_date"
        )
        .reset_index(drop=True)
    )

    total_reps = len(sales_reps)

    top_cutoff = max(
        1,
        round(total_reps * 0.30)
    )

    middle_cutoff = max(
        top_cutoff + 1,
        round(total_reps * 0.70)
    )

    top_ids = (
        sales_reps.iloc[
            :top_cutoff
        ]["employee_id"]
        .tolist()
    )

    middle_ids = (
        sales_reps.iloc[
            top_cutoff:middle_cutoff
        ]["employee_id"]
        .tolist()
    )

    newer_ids = (
        sales_reps.iloc[
            middle_cutoff:
        ]["employee_id"]
        .tolist()
    )

    # Safety fallback
    if not middle_ids:
        middle_ids = top_ids.copy()

    if not newer_ids:
        newer_ids = middle_ids.copy()

    # ------------------------------------------
    # Round-Robin Assignment
    # ------------------------------------------

    top_index = 0
    middle_index = 0
    newer_index = 0

    assignments = []

    for _, customer in customers.iterrows():

        activity = customer["activity_level"]

        rules = ACCOUNT_ASSIGNMENT_WEIGHTS[
            activity
        ]

        tier = random.choices(

            rules["tiers"],

            weights=rules["weights"],

            k=1

        )[0]

        if tier == "Top":

            employee_id = top_ids[top_index]

            top_index = (
                top_index + 1
            ) % len(top_ids)

        elif tier == "Middle":

            employee_id = middle_ids[middle_index]

            middle_index = (
                middle_index + 1
            ) % len(middle_ids)

        else:

            employee_id = newer_ids[newer_index]

            newer_index = (
                newer_index + 1
            ) % len(newer_ids)

        assignments.append(employee_id)

    customers[
        "sales_rep_id"
    ] = assignments

    customers = (
        customers
        .drop(
            columns="_activity_rank"
        )
        .sort_values(
            by="customer_id"
        )
        .reset_index(drop=True)
    )


    return customers

# ======================================================
# Generate Customers
# ======================================================

def generate_customers():
    """
    Generates the LOTS Corp. Customer Master.
    """

    print("Generating customers...")

    supplier_reference = load_supplier_reference_data()

    customer_state = initialize_customer_state()

    customers = []

    for customer_number in range(1, TOTAL_CUSTOMERS + 1):

        customer_id = f"CUS{customer_number:04d}"

        customer_type, industry = (
            generate_customer_classification()
        )

        company_name = generate_company_name(
            customer_type,
            supplier_reference,
            customer_state
        )

        contact_person = generate_contact_person(
            supplier_reference,
            customer_state
        )

        company_domain = generate_company_domain(
            company_name,
            supplier_reference,
            customer_state
        )

        email = generate_customer_email(
            contact_person,
            company_domain,
            supplier_reference,
            customer_state
        )

        mobile_number = generate_customer_mobile(
            supplier_reference,
            customer_state
        )

        city, province, region = (
            generate_customer_location()
        )

        credit_limit = generate_credit_limit(
            customer_type
        )

        payment_terms = (
            generate_customer_payment_terms(
                customer_type
            )
        )

        status = generate_customer_status()

        created_at = fake.date_between(
            start_date="-5y",
            end_date="-1y"
        )

        updated_at = fake.date_between(
            start_date=created_at,
            end_date="today"
        )

        customers.append({

            "customer_id": customer_id,

            "customer_name": company_name,

            "customer_type": customer_type,

            "industry": industry,

            "contact_person": contact_person,

            "email": email,

            "mobile_number": mobile_number,

            "city": city,

            "province": province,

            "region": region,

            "credit_limit": credit_limit,

            "payment_terms": payment_terms,

            "status": status,

            "created_at": created_at,

            "updated_at": updated_at

        })

    customers_df = pd.DataFrame(customers)

    customers_df.to_csv(        # This should use the function for saving csv not the method of df .to_csv()
        RAW_DIR / "customers.csv",
        index=False
    )

    print(
        f"✓ {len(customers_df)} customers generated."
    )

    print("✓ customers.csv saved.")

    return customers_df

# ======================================================
# Validate Customers
# ======================================================

def validate_customers(customers_df):
    """
    Validates the generated Customer Master.
    """

    print("\nRunning customer validations...")

    # --------------------------------------------------
    # Customer IDs
    # --------------------------------------------------

    assert customers_df["customer_id"].is_unique
    print("✓ Customer IDs are unique")

    # --------------------------------------------------
    # Customer Names
    # --------------------------------------------------

    assert customers_df["customer_name"].is_unique
    print("✓ Customer names are unique")

    # --------------------------------------------------
    # Contact Persons
    # --------------------------------------------------

    assert customers_df["contact_person"].is_unique
    print("✓ Contact persons are unique")

    # --------------------------------------------------
    # Emails
    # --------------------------------------------------

    assert customers_df["email"].is_unique
    print("✓ Emails are unique")

    # --------------------------------------------------
    # Mobile Numbers
    # --------------------------------------------------

    assert customers_df["mobile_number"].is_unique
    print("✓ Mobile numbers are unique")

    # --------------------------------------------------
    # Supplier Cross Validation
    # --------------------------------------------------

    supplier_df = pd.read_csv(
        RAW_DIR / "suppliers.csv"
    )

    assert (
        set(customers_df["email"])
        .isdisjoint(
            supplier_df["email"]
        )
    )

    assert (
        set(customers_df["mobile_number"])
        .isdisjoint(
            supplier_df["mobile_number"]
        )
    )

    assert (
        set(customers_df["contact_person"])
        .isdisjoint(
            supplier_df["contact_person"]
        )
    )

    print("✓ Supplier cross-validation passed")

    # --------------------------------------------------
    # Credit Limit
    # --------------------------------------------------

    assert (customers_df["credit_limit"] > 0).all()
    print("✓ Credit limits validated")

    # --------------------------------------------------
    # Customer Type
    # --------------------------------------------------

    valid_customer_types = set(CUSTOMER_TYPES.keys())

    assert customers_df["customer_type"].isin(
        valid_customer_types
    ).all()

    print("✓ Customer types validated")

    # --------------------------------------------------
    # Industry
    # --------------------------------------------------

    for _, row in customers_df.iterrows():

        assert row["industry"] in INDUSTRIES[
            row["customer_type"]
        ]

    print("✓ Industries validated")

    # --------------------------------------------------
    # Payment Terms
    # --------------------------------------------------

    for _, row in customers_df.iterrows():

        assert row["payment_terms"] in \
            CUSTOMER_PAYMENT_TERMS[
                row["customer_type"]
            ]

    print("✓ Payment terms validated")

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    assert customers_df["status"].isin(
        ["Active", "Inactive"]
    ).all()

    print("✓ Customer status validated")

    # --------------------------------------------------
    # Timestamp Validation
    # --------------------------------------------------

    created = pd.to_datetime(
        customers_df["created_at"]
    )

    updated = pd.to_datetime(
        customers_df["updated_at"]
    )

    assert (updated >= created).all()

    print("✓ Timestamp validation passed")

    print("\nALL CUSTOMER VALIDATIONS PASSED\n")

# ======================================================
# GENERATE PRODUCTS
# ======================================================

def generate_products(suppliers_df):

    print("Generating products...")

    # --------------------------------------------------
    # Create Supplier Lookup
    # --------------------------------------------------

    supplier_lookup = dict(
        zip(
            suppliers_df["supplier_name"],
            suppliers_df["supplier_id"]
        )
    )

    products = []

    product_counter = 1

    # --------------------------------------------------
    # Build Products
    # --------------------------------------------------

    for family in PRODUCT_FAMILIES:

        supplier_id = supplier_lookup[family["supplier"]]

        for variant in family["variants"]:

            variant_name = variant["name"]
            variant_factor = variant["factor"]

            category = family["category"]
            brand = family["brand"]

            # Product Name

            product_name = f"{family['family']} {variant_name}"

            # Product Family

            product_family = family["family"]

            # --------------------------------------------------
            # Product ID
            # --------------------------------------------------

            product_id = f"PROD{product_counter:04d}"

            # --------------------------------------------------
            # Price Generation (Version 0.6)
            # --------------------------------------------------

            base_price = FAMILY_BASE_PRICE[product_family]

            brand_multiplier = BRAND_MULTIPLIERS[brand]

            random_factor = random.uniform(0.96, 1.04)

            selling_price = round(
                base_price
                * brand_multiplier
                * variant_factor
                * random_factor,
                2
            )

            margin = random.uniform(0.18, 0.32)

            cost_price = round(
                selling_price * (1 - margin),
                2
            )

            # --------------------------------------------------
            # Launch Date
            # --------------------------------------------------

            launch_date = fake.date_between(
                start_date="-3y",
                end_date="today"
            )

            # --------------------------------------------------
            # Timestamps
            # --------------------------------------------------

            created_at = launch_date

            updated_at = fake.date_between(
                start_date=launch_date,
                end_date="today"
            )

            # --------------------------------------------------
            # Reorder Level
            # --------------------------------------------------

            reorder_level = random.choice(
                [5, 10, 15, 20, 25]
            )

            # --------------------------------------------------
            # Active Flag
            # --------------------------------------------------

            active = random.choices(
                [True, False],
                weights=[90, 10],
                k=1
            )[0]

            # --------------------------------------------------
            # Meaningful SKU
            # --------------------------------------------------

            brand_code = "".join(
                [c for c in brand.upper() if c.isalpha()]
            )[:3]

            category_code = category.upper()[:3]

            sku = (
                f"{category_code}-"
                f"{brand_code}-"
                f"{product_counter:04d}"
            )

            # --------------------------------------------------
            # Append
            # --------------------------------------------------

            products.append({

                "product_id": product_id,

                "product_name": product_name,

                "product_family": product_family,

                "variant": variant_name,

                "brand": brand,

                "category": category,

                "description": family["description"],

                "sku": sku,

                "supplier_id": supplier_id,

                "cost_price": cost_price,

                "selling_price": selling_price,

                "reorder_level": reorder_level,

                "active": active,

                "launch_date": launch_date,

                "created_at": created_at,

                "updated_at": updated_at

            })

            product_counter += 1

    # --------------------------------------------------
    # DataFrame
    # --------------------------------------------------

    products_df = pd.DataFrame(products)

    print(f"✓ {len(products_df)} products generated.")

    products_df.to_csv(

        RAW_DIR / "products.csv",

        index=False,

        encoding="utf-8-sig"

    )

    print("✓ products.csv saved.")

    return products_df

# ======================================================
# VALIDATE PRODUCTS
# ======================================================

def validate_products(products_df, suppliers_df):

    print("\nRunning product validations...")

    # ----------------------------------------------
    # Product ID
    # ----------------------------------------------

    assert products_df["product_id"].is_unique, \
        "Duplicate Product IDs found."

    print("✓ Product IDs are unique")

    # ----------------------------------------------
    # Product Name
    # ----------------------------------------------

    assert products_df["product_name"].is_unique, \
        "Duplicate Product Names found."

    print("✓ Product names are unique")

    # ----------------------------------------------
    # SKU
    # ----------------------------------------------

    assert products_df["sku"].is_unique, \
        "Duplicate SKUs found."

    print("✓ SKUs are unique")

    # ----------------------------------------------
    # Supplier FK
    # ----------------------------------------------

    valid_supplier_ids = set(suppliers_df["supplier_id"])

    assert products_df["supplier_id"].isin(
        valid_supplier_ids
    ).all(), \
        "Invalid supplier_id found."

    print("✓ Supplier references are valid")

    # ----------------------------------------------
    # Prices
    # ----------------------------------------------

    assert (
        products_df["selling_price"]
        >
        products_df["cost_price"]
    ).all(), \
        "Selling price must exceed cost price."

    print("✓ Selling prices validated")

    # ----------------------------------------------
    # Dates
    # ----------------------------------------------

    assert (
        products_df["created_at"]
        <=
        products_df["updated_at"]
    ).all(), \
        "created_at later than updated_at."

    print("✓ Timestamp validation passed")

    print("\nALL PRODUCT VALIDATIONS PASSED\n")

# ======================================================
# Order State
# ======================================================

def initialize_order_state():

    """
    Tracks state while generating orders.
    """

    return {

        "used_order_ids": set()

    }

# ======================================================
# Build Order Blueprints
# ======================================================

def build_order_blueprints(
    reference_data
):
    """
    Builds all order blueprints before
    creating the final order records.
    """

    blueprints = []

    customers = reference_data[
        "customers"
    ]

    sales_reps = reference_data[
        "sales_reps"
    ]

    # ------------------------------------------
    # Sales Representative Lookup
    # ------------------------------------------

    sales_rep_lookup = (
        sales_reps
        .set_index(
            "employee_id"
        )
    )

    # ------------------------------------------
    # Build Blueprints
    # ------------------------------------------

    for _, customer in customers.iterrows():

        order_capacity = customer[
            "order_capacity"
        ]

        sales_rep_hire_date = (
            sales_rep_lookup.loc[
                customer["sales_rep_id"],
                "hire_date"
            ]
        )

        order_dates = (
            generate_customer_order_dates(

                order_capacity,

                customer[
                    "activity_level"
                ],

                customer[
                    "created_at"
                ],

                sales_rep_hire_date

            )
        )

        order_dates.sort()

        for order_date in order_dates:

            blueprint = {

                "order_id":
                    generate_order_id(
                        len(
                            blueprints
                        ) + 1
                    ),

                "customer_id":
                    customer[
                        "customer_id"
                    ],

                "sales_rep_id":
                    customer[
                        "sales_rep_id"
                    ],

                "order_date":
                    order_date

            }

            blueprints.append(
                blueprint
            )

    # ------------------------------------------
    # Summary
    # ------------------------------------------

    print()

    print("=" * 60)

    print(
        "Order Blueprint Summary"
    )

    print("=" * 60)

    print(
        "Blueprints:",
        len(
            blueprints
        )
    )

    print()

    print("Preview:")

    for blueprint in blueprints[:5]:

        print(
            blueprint
        )

    customer_accounts = (
        customers[
            [
                "customer_id",
                "sales_rep_id"
            ]
        ]
    )

    print()

    print("=" * 60)

    print(
        "Customer Account Managers"
    )

    print("=" * 60)

    print(
        customer_accounts.head(10)
    )

    print()

    print("=" * 60)

    print(
        "Customer Portfolio by Sales Representative"
    )

    print("=" * 60)

    portfolio = (
        customers
        .groupby(
            "sales_rep_id"
        )[
            "order_capacity"
        ]
        .agg(
            [
                "count",
                "sum"
            ]
        )
    )

    portfolio.columns = [

        "customers",

        "planned_orders"

    ]

    print(
        portfolio
    )

    return blueprints


def random_date_between(
    start_date,
    end_date
):
    """
    Returns a random datetime
    between two dates.
    """

    total_days = (
        end_date - start_date
    ).days

    random_days = random.randint(
        0,
        total_days
    )

    return (
        start_date
        +
        timedelta(days=random_days)
    )

def choose_order_month():
    """
    Returns a month number (1-12)
    using business seasonality.
    """

    months = list(
        MONTHLY_ORDER_WEIGHTS.keys()
    )

    weights = list(
        MONTHLY_ORDER_WEIGHTS.values()
    )

    return random.choices(
        months,
        weights=weights,
        k=1
    )[0]

def choose_order_day(
    year,
    month
):
    """
    Returns a valid day
    for the given year and month.
    """

    max_day = calendar.monthrange(
        year,
        month
    )[1]

    return random.randint(
        1,
        max_day
    )

def generate_customer_order_dates(
    order_count,
    activity_level,
    customer_created_at,
    sales_rep_hire_date
):
    """
    Generates every order date for one customer.

    This version is scalable to hundreds of
    thousands or millions of orders because
    multiple orders are allowed on the same day.

    Returns
    -------
    list[pandas.Timestamp]
    """

    start_date = max(

        pd.to_datetime(customer_created_at),

        pd.to_datetime(sales_rep_hire_date),

        pd.Timestamp(ORDER_START_DATE)

    )

    end_date = pd.Timestamp(ORDER_END_DATE)

    if start_date > end_date:

        return []

    order_dates = []

    while len(order_dates) < order_count:

        # -------------------------------
        # Pick month using seasonality
        # -------------------------------

        year = random.randint(

            start_date.year,

            end_date.year

        )

        month = choose_order_month()

        day = choose_order_day(

            year,

            month

        )

        try:

            candidate = pd.Timestamp(

                year=year,

                month=month,

                day=day

            )

        except ValueError:

            continue

        # -------------------------------
        # Date must be valid
        # -------------------------------

        if candidate < start_date:

            continue

        if candidate > end_date:

            continue

        order_dates.append(candidate)

    order_dates.sort()

    return order_dates

def generate_order_status(
    order_date
):
    """
    Generates a realistic order status
    based on the age of the order.
    """
    order_age = (
        DATASET_END_DATE
        -
        order_date
    ).days

    for stage in ORDER_STATUS_RULES.values():

        if order_age <= stage["max_days"]:

            statuses = list(
                stage["weights"].keys()
            )

            weights = list(
                stage["weights"].values()
            )

            return random.choices(

                statuses,

                weights=weights,

                k=1

            )[0]

def generate_payment_status(
    order_status
):
    """
    Generates payment status
    based on the order status.
    """

    rules = PAYMENT_STATUS_RULES[
        order_status
    ]

    return random.choices(

        list(rules.keys()),

        weights=list(rules.values()),

        k=1

    )[0]

def generate_order_updated_timestamp(
    created_at
):
    """
    Generates a realistic updated timestamp
    on or after created_at.
    """

    end = DATASET_END_DATE

    if isinstance(
        end,
        pd.Timestamp
    ):

        end = end.to_pydatetime()

    if created_at >= end:

        return created_at

    seconds = int(
        (end - created_at).total_seconds()
    )

    random_seconds = random.randint(
        0,
        seconds
    )

    return created_at + timedelta(
        seconds=random_seconds
    )


def build_order_record(
    blueprint,
    reference_data
):
    """
    Builds one complete order record
    from an order blueprint.
    """

    # ------------------------------------------
    # Order Date
    # ------------------------------------------

    order_date = blueprint[
        "order_date"
    ]

    order_age = (
        DATASET_END_DATE
        - order_date
    ).days

    # ------------------------------------------
    # Order Status
    # ------------------------------------------

    order_status = generate_order_status( # This is my fix to the error below
        order_date
    )

    # ------------------------------------------
    # Payment Status
    # ------------------------------------------

    payment_status = generate_payment_status(
        order_status
    )

    # ------------------------------------------
    # Order Source
    # ------------------------------------------

    order_source = random.choices(

        list(
            ORDER_SOURCE.keys()
        ),

        weights=list(
            ORDER_SOURCE.values()
        ),

        k=1

    )[0]

    # ------------------------------------------
    # Record Timestamps
    # ------------------------------------------

    created_at = generate_order_created_timestamp(
        order_date
    )

    updated_at = generate_order_updated_timestamp(
        created_at
    )

    # ------------------------------------------
    # Build Record
    # ------------------------------------------

    order = {

        "order_id":
            blueprint["order_id"],

        "customer_id":
            blueprint["customer_id"],

        "sales_rep_id":
            blueprint["sales_rep_id"],

        "order_date":
            order_date,

        "order_status":
            order_status,

        "payment_status":
            payment_status,

        "order_source":
            order_source,

        "created_at":
            created_at,

        "updated_at":
            updated_at

    }

    return order

def validate_unique_order_ids(
    orders_df
):
    """
    Validates that every Order ID
    is unique.
    """

    if orders_df[
        "order_id"
    ].duplicated().any():

        raise ValueError(
            "Duplicate Order IDs found."
        )

    print(
        "✓ Order IDs are unique"
    )

def validate_customer_references(
    orders_df,
    reference_data
):
    """
    Validates customer references.
    """

    valid_customers = set(

        reference_data[
            "customers"
        ]["customer_id"]

    )

    invalid = orders_df[
        ~orders_df[
            "customer_id"
        ].isin(valid_customers)
    ]

    if not invalid.empty:

        raise ValueError(
            "Invalid customer references found."
        )

    print(
        "✓ Customer references are valid"
    )

def validate_sales_rep_references(
    orders_df,
    reference_data
):
    """
    Validates Sales Representative references.
    """

    valid_sales_reps = set(

        reference_data[
            "sales_reps"
        ]["employee_id"]

    )

    invalid = orders_df[
        ~orders_df[
            "sales_rep_id"
        ].isin(valid_sales_reps)
    ]

    if not invalid.empty:

        raise ValueError(
            "Invalid Sales Representative references found."
        )

    print(
        "✓ Sales Representative references are valid"
    )

def validate_order_dates(
    orders_df,
    reference_data
):
    """
    Validates order dates.
    """

    if (
        orders_df[
            "order_date"
        ] > DATASET_END_DATE
    ).any():

        raise ValueError(
            "Orders exist beyond DATASET_END_DATE."
        )

    print(
        "✓ Order dates validated"
    )

def validate_order_status(
    orders_df
):
    """
    Validates order status values.
    """

    valid_status = set()

    for stage in ORDER_STATUS_RULES.values():

        valid_status.update(

            stage[
                "weights"
            ].keys()

        )

    invalid = set(

        orders_df[
            "order_status"
        ]

    ) - valid_status

    if invalid:

        raise ValueError(
            f"Invalid order status: {invalid}"
        )

    print(
        "✓ Order statuses validated"
    )

def validate_payment_status(
    orders_df
):
    """
    Validates payment status values.
    """

    valid_status = set()

    for rules in PAYMENT_STATUS_RULES.values():

        valid_status.update(
            rules.keys()
        )

    invalid = set(

        orders_df[
            "payment_status"
        ]

    ) - valid_status

    if invalid:

        raise ValueError(
            f"Invalid payment status: {invalid}"
        )

    print(
        "✓ Payment statuses validated"
    )

def validate_order_source(
    orders_df
):
    """
    Validates order sources.
    """

    invalid = set(

        orders_df[
            "order_source"
        ]

    ) - set(
        ORDER_SOURCE.keys()
    )

    if invalid:

        raise ValueError(
            f"Invalid order source: {invalid}"
        )

    print(
        "✓ Order sources validated"
    )

def validate_order_timestamps(
    orders_df
):
    """
    Validates order timestamps.
    """

    invalid = orders_df[

        orders_df[
            "updated_at"
        ]
        <
        orders_df[
            "created_at"
        ]

    ]

    if not invalid.empty:

        raise ValueError(
            "Invalid order timestamps."
        )

    print(
        "✓ Timestamp validation passed"
    )

def validate_orders(
    orders_df,
    reference_data
):
    """
    Runs all validations
    for the Orders table.
    """

    print()
    print("Running order validations...")

    validate_unique_order_ids(
        orders_df
    )

    validate_customer_references(
        orders_df,
        reference_data
    )

    validate_sales_rep_references(
        orders_df,
        reference_data
    )

    validate_order_dates(
        orders_df,
        reference_data
    )

    validate_order_status(
        orders_df
    )

    validate_payment_status(
        orders_df
    )

    validate_order_source(
        orders_df
    )

    validate_order_timestamps(
        orders_df
    )

    print()
    print(
        "ALL ORDER VALIDATIONS PASSED"
    )

    print()


def generate_order_created_timestamp(
    order_date
):
    """
    Generates a realistic created timestamp
    on the same calendar day as the order.
    """

    if isinstance(
        order_date,
        pd.Timestamp
    ):

        order_date = order_date.to_pydatetime()

    start = datetime.combine(
        order_date.date(),
        datetime.min.time()
    )

    end = datetime.combine(
        order_date.date(),
        datetime.max.time()
    )

    seconds = int(
        (end - start).total_seconds()
    )

    random_seconds = random.randint(
        0,
        seconds
    )

    return start + timedelta(
        seconds=random_seconds
    )

def generate_orders(
    reference_data
):
    """
    Generates the Orders table.
    """

    print()
    print("Generating orders...")

    # ------------------------------------------
    # Build Blueprints
    # ------------------------------------------

    blueprints = build_order_blueprints(
        reference_data
    )

    # ------------------------------------------
    # Build Records
    # ------------------------------------------

    orders = []

    for blueprint in blueprints:

        order = build_order_record(
            blueprint,
            reference_data
        )

        orders.append(order)

    # ------------------------------------------
    # Create DataFrame
    # ------------------------------------------

    orders_df = pd.DataFrame(
        orders
    )

    # ------------------------------------------
    # Validate
    # ------------------------------------------

    validate_orders(
        orders_df,
        reference_data
    )

    # ------------------------------------------
    # Save CSV
    # ------------------------------------------

    save_csv(
        orders_df,
        "orders.csv"
    )

    print(
        f"✓ {len(orders_df)} orders generated."
    )

    print(
        "✓ orders.csv saved."
    )

    return orders_df

def choose_products_for_order(
    products_df,
    number_of_products
):
    """
    Selects unique products for one order.

    Products are chosen using weighted
    probabilities based on product category.

    No duplicate products are allowed
    within the same order.

    Returns
    -------
    pandas.DataFrame
    """

    available_products = (
        products_df.copy()
    )

    available_products[
        "selection_weight"
    ] = (

        available_products[
            "category"
        ]

        .map(
            CATEGORY_ORDER_WEIGHT
        )

    )

    selected_products = []

    while (

        len(selected_products)
        < number_of_products

    ):

        selected = (

            available_products.sample(

                n=1,

                weights=
                "selection_weight"

            )

        )

        selected_products.append(
            selected
        )

        available_products = (

            available_products[

                available_products[
                    "product_id"
                ]

                !=

                selected.iloc[0][
                    "product_id"
                ]

            ]

        )

    selected_products = pd.concat(

        selected_products,

        ignore_index=True

    )

    selected_products = (

        selected_products.drop(
            columns="selection_weight"
        )

    )

    return selected_products

def choose_number_of_products():
    """
    Returns the number of products
    that belong to one order.
    """

    return random.choices(

        list(
            ORDER_PRODUCT_COUNT.keys()
        ),

        weights=list(
            ORDER_PRODUCT_COUNT.values()
        ),

        k=1

    )[0]
    
def choose_order_quantity():
    """
    Returns the ordered quantity
    for one product.
    """

    return random.choices(

        list(
            ORDER_QUANTITY.keys()
        ),

        weights=list(
            ORDER_QUANTITY.values()
        ),

        k=1

    )[0]

def build_order_detail_record(
    order_detail_id,
    order,
    product
):
    """
    Builds one complete order detail record.

    One record represents one product
    purchased within one order.
    """

    # ------------------------------------------
    # Quantity
    # ------------------------------------------

    quantity = choose_order_quantity()

    # ------------------------------------------
    # Unit Cost & Selling Price
    # ------------------------------------------

    unit_cost = product[
        "cost_price"
    ]

    unit_price = product[
        "selling_price"
    ]

    # ------------------------------------------
    # Discount
    # ------------------------------------------

    discount_pct = random.choices(

        list(
            DISCOUNT_PERCENTAGES.keys()
        ),

        weights=list(
            DISCOUNT_PERCENTAGES.values()
        ),

        k=1

    )[0]

    # ------------------------------------------
    # Financial Calculations
    # ------------------------------------------

    gross_amount = (
        quantity
        * unit_price
    )

    discount_amount = (
        gross_amount
        * discount_pct
    )
    
    line_total = np.round(
        gross_amount
        - discount_amount,
        2
    )

    line_cost = round(

        quantity
        * unit_cost,

        2

    )

    line_profit = round(

        line_total
        - line_cost,

        2

    )

    # ------------------------------------------
    # Build Record
    # ------------------------------------------

    order_detail = {

        "order_detail_id":
            order_detail_id,

        "order_id":
            order["order_id"],

        "product_id":
            product["product_id"],

        "quantity":
            quantity,

        "unit_cost":
            unit_cost,

        "unit_price":
            unit_price,

        "discount_pct":
            discount_pct,

        "line_total":
            line_total,

        "line_cost":
            line_cost,

        "line_profit":
            line_profit,

        "created_at":
            order["created_at"],

        "updated_at":
            order["updated_at"]

    }

    return order_detail

def validate_order_detail_ids(
    order_details_df
):
    """
    Validates order detail IDs.
    """

    if order_details_df[
        "order_detail_id"
    ].duplicated().any():

        raise ValueError(
            "Duplicate order_detail_id found."
        )

    print(
        "✓ Order Detail IDs are unique"
    )

def validate_order_detail_order_references(
    order_details_df,
    orders_df
):
    """
    Validates order references.
    """

    valid_orders = set(
        orders_df["order_id"]
    )

    invalid = (
        ~order_details_df[
            "order_id"
        ].isin(valid_orders)
    )

    if invalid.any():

        raise ValueError(
            "Invalid order_id reference."
        )

    print(
        "✓ Order references are valid"
    )

def validate_order_detail_product_references(
    order_details_df,
    products_df
):
    """
    Validates product references.
    """

    valid_products = set(
        products_df["product_id"]
    )

    invalid = (
        ~order_details_df[
            "product_id"
        ].isin(valid_products)
    )

    if invalid.any():

        raise ValueError(
            "Invalid product_id reference."
        )

    print(
        "✓ Product references are valid"
    )

def validate_order_detail_quantities(
    order_details_df
):
    """
    Validates quantities.
    """

    if (
        order_details_df[
            "quantity"
        ] <= 0
    ).any():

        raise ValueError(
            "Invalid quantity."
        )

    print(
        "✓ Quantities validated"
    )

def validate_order_detail_prices(
    order_details_df
):
    """
    Validates prices.
    """

    if (
        order_details_df[
            "unit_cost"
        ] <= 0
    ).any():

        raise ValueError(
            "Invalid unit_cost."
        )

    if (
        order_details_df[
            "unit_price"
        ] <= 0
    ).any():

        raise ValueError(
            "Invalid unit_price."
        )

    print(
        "✓ Prices validated"
    )

def validate_order_detail_discounts(
    order_details_df
):
    """
    Validates discounts.
    """

    if (
        order_details_df[
            "discount_pct"
        ] < 0
    ).any():

        raise ValueError(
            "Negative discount found."
        )

    if (
        order_details_df[
            "discount_pct"
        ] > 1
    ).any():

        raise ValueError(
            "Discount exceeds 100%."
        )

    print(
        "✓ Discounts validated"
    )

def validate_order_detail_financials(
    order_details_df
):
    """
    Recalculates financial values
    and validates stored totals.
    """

    expected_total = (

        (order_details_df["quantity"]

        * order_details_df["unit_price"]) - ((order_details_df["quantity"]

        * order_details_df["unit_price"]) * order_details_df["discount_pct"])

    ).round(2)

    expected_cost = (

        order_details_df["quantity"]

        * order_details_df[
            "unit_cost"
        ]

    ).round(2)

    expected_profit = (
        expected_total
        - expected_cost
    ).round(2)

    print("Is it equal:", (expected_total == order_details_df["line_total"]).all())
    print("expected_total:", expected_total)
    print("line_total:", order_details_df["line_total"])

    if not (
        expected_total
        ==
        order_details_df[
            "line_total"
        ]
    ).all():

        raise ValueError(
            "line_total validation failed."
        )

    if not (
        expected_cost
        ==
        order_details_df[
            "line_cost"
        ]
    ).all():

        raise ValueError(
            "line_cost validation failed."
        )

    if not (
        expected_profit
        ==
        order_details_df[
            "line_profit"
        ]
    ).all():

        raise ValueError(
            "line_profit validation failed."
        )

    print(
        "✓ Financial calculations validated"
    )

def validate_order_detail_timestamps(
    order_details_df
):
    """
    Validates timestamps.
    """

    invalid = (

        order_details_df[
            "updated_at"
        ]

        <

        order_details_df[
            "created_at"
        ]

    )

    if invalid.any():

        raise ValueError(
            "Invalid timestamps."
        )

    print(
        "✓ Timestamp validation passed"
    )

def validate_order_details(
    order_details_df,
    orders_df,
    products_df
):
    """
    Runs all order detail validations.
    """

    print()
    print(
        "Running order detail validations..."
    )

    validate_order_detail_ids(
        order_details_df
    )

    validate_order_detail_order_references(
        order_details_df,
        orders_df
    )

    validate_order_detail_product_references(
        order_details_df,
        products_df
    )

    validate_order_detail_quantities(
        order_details_df
    )

    validate_order_detail_prices(
        order_details_df
    )

    validate_order_detail_discounts(
        order_details_df
    )

    validate_order_detail_financials(
        order_details_df
    )

    validate_order_detail_timestamps(
        order_details_df
    )

    print()
    print(
        "ALL ORDER DETAIL VALIDATIONS PASSED"
    )

def generate_order_details():
    """
    Generates one Order Detail record
    for every product purchased
    in every Order.
    """

    print(
        "Generating order details..."
    )

    # ------------------------------------------
    # Load Reference Data
    # ------------------------------------------

    reference_data = (
        load_order_details_reference_data()
    )

    orders_df = reference_data[
        "orders"
    ]

    products_df = reference_data[
        "products"
    ]

    order_details = []

    detail_counter = 1

    # ------------------------------------------
    # Build Order Details
    # ------------------------------------------

    for _, order in orders_df.iterrows():

        number_of_products = (
            choose_number_of_products()
        )

        selected_products = (
            choose_products_for_order(

                products_df,

                number_of_products

            )
        )

        for _, product in (
            selected_products.iterrows()
        ):

            detail = (
                build_order_detail_record(

                    f"DET{detail_counter:06d}",

                    order,

                    product

                )
            )

            order_details.append(
                detail
            )

            detail_counter += 1

    # ------------------------------------------
    # DataFrame
    # ------------------------------------------

    order_details_df = pd.DataFrame(
        order_details
    )

    # ------------------------------------------
    # Validation
    # ------------------------------------------

    validate_order_details(

        order_details_df,

        orders_df,

        products_df

    )

    # ------------------------------------------
    # Save
    # ------------------------------------------

    save_csv(

        order_details_df,

        "order_details.csv"

    )

    print(
        f"✓ {len(order_details_df)} order details generated."
    )

    print(
        "✓ order_details.csv saved."
    )

    return order_details_df

def assign_product_warehouse(
    products_df
):
    """
    Assigns each product to a warehouse
    according to its product category.

    Returns
    -------
    DataFrame
    """

    products = products_df.copy()

    warehouse_lookup = {}

    for warehouse in WAREHOUSES:

        warehouse_name = warehouse[
            "warehouse_name"
        ]

        warehouse_id = warehouse[
            "warehouse_id"
        ]

        categories = (
            WAREHOUSE_PRODUCT_MAP[
                warehouse_name
            ]
        )

        for category in categories:

            warehouse_lookup[
                category
            ] = warehouse_id

    products["warehouse_id"] = (

        products["category"]
        .map(warehouse_lookup)

    )

    if (

        products["warehouse_id"]
        .isna()
        .any()

    ):

        missing_categories = (

            products.loc[

                products[
                    "warehouse_id"
                ].isna(),

                "category"

            ]
            .unique()

        )

        raise ValueError(

            "Warehouse assignment missing for "
            f"categories: {missing_categories}"

        )

    return products

def summarize_product_sales(
    products_df,
    orders_df,
    order_details_df
):
    """
    Creates one sales summary
    for every product.

    The summary is later used
    to generate realistic
    inventory levels.

    Returns
    -------
    DataFrame
    """

    # ------------------------------------------
    # Merge Orders with Order Details
    # ------------------------------------------

    sales = (

        order_details_df

        .merge(

            orders_df[
                [
                    "order_id",
                    "order_date"
                ]
            ],

            on="order_id",

            how="left"

        )

    )

    # ------------------------------------------
    # Product Sales Summary
    # ------------------------------------------

    sales_summary = (

        sales

        .groupby(
            "product_id"
        )

        .agg(

            total_units_sold=(

                "quantity",
                "sum"

            ),

            total_orders=(

                "order_id",
                "nunique"

            ),

            last_sale_date=(

                "order_date",
                "max"

            )

        )

        .reset_index()

    )

    # ------------------------------------------
    # Merge with Product Master
    # ------------------------------------------

    inventory_reference = (

        products_df

        .merge(

            sales_summary,

            on="product_id",

            how="left"

        )

    )

    # ------------------------------------------
    # Fill Products with No Sales
    # ------------------------------------------

    inventory_reference[
        "total_units_sold"
    ] = (

        inventory_reference[
            "total_units_sold"
        ]

        .fillna(0)

        .astype(int)

    )

    inventory_reference[
        "total_orders"
    ] = (

        inventory_reference[
            "total_orders"
        ]

        .fillna(0)

        .astype(int)

    )

    # ------------------------------------------
    # Preview
    # ------------------------------------------

    print()

    print("=" * 60)

    print("Product Sales Summary")

    print("=" * 60)

    print(

        inventory_reference[
            [

                "product_id",

                "product_name",

                "warehouse_id",

                "total_units_sold",

                "total_orders",

                "last_sale_date"

            ]

        ].head(10)

    )

    return inventory_reference

def classify_sales_velocity(
    total_units_sold
):
    """
    Classifies products according
    to total units sold.
    """

    if total_units_sold >= 50000:

        return "Fast"

    elif total_units_sold >= 15000:

        return "Medium"

    else:

        return "Slow"

def choose_inventory_coverage(
    sales_velocity
):
    """
    Returns inventory coverage
    in months.
    """

    if sales_velocity == "Fast":

        table = FAST_MOVING_MONTHS

    elif sales_velocity == "Medium":

        table = MEDIUM_MOVING_MONTHS

    else:

        table = SLOW_MOVING_MONTHS

    return random.choices(

        list(table.keys()),

        weights=list(table.values()),

        k=1

    )[0]

def choose_reserved_percentage():
    """
    Returns reserved stock percentage.
    """

    return random.choices(

        list(
            RESERVED_STOCK_PERCENTAGES.keys()
        ),

        weights=list(
            RESERVED_STOCK_PERCENTAGES.values()
        ),

        k=1

    )[0]

def build_inventory_record(
    inventory_id,
    product
):
    """
    Builds one inventory record
    for one product.
    """

    # ------------------------------------------
    # Sales Velocity
    # ------------------------------------------

    sales_velocity = classify_sales_velocity(
        product["total_units_sold"]
    )

    # ------------------------------------------
    # Inventory Coverage
    # ------------------------------------------

    coverage_months = choose_inventory_coverage(
        sales_velocity
    )

    # ------------------------------------------
    # Average Monthly Sales
    # ------------------------------------------

    average_monthly_sales = (
        product["total_units_sold"]
        / INVENTORY_MONTHS
    )

    # ------------------------------------------
    # Current Stock
    # ------------------------------------------

    if product["total_units_sold"] == 0:

        current_stock = round(

            product["reorder_level"]

            * random.uniform(
                2.0,
                5.0
            )

        )

    else:

        planned_stock = (

            average_monthly_sales
            * coverage_months

        )

        planning_variance = random.uniform(

            0.90,
            1.10

        )

        current_stock = max(

            0,

            round(

                planned_stock
                * planning_variance

            )

        )

    # ------------------------------------------
    # Reserved Stock
    # ------------------------------------------

    reserved_percentage = (
        choose_reserved_percentage()
    )

    reserved_stock = round(

        current_stock
        * reserved_percentage

    )

    # ------------------------------------------
    # Available Stock
    # ------------------------------------------

    available_stock = max(

        0,

        current_stock
        - reserved_stock

    )

    # ------------------------------------------
    # Inventory Status
    # ------------------------------------------

    reorder_level = product[
        "reorder_level"
    ]

    if available_stock == 0:

        inventory_status = (
            "Out of Stock"
        )

    elif available_stock <= reorder_level:

        inventory_status = (
            "Low Stock"
        )

    else:

        inventory_status = (
            "In Stock"
        )

    # ------------------------------------------
    # Last Stock Movement
    # ------------------------------------------

    last_stock_movement = product[
        "last_sale_date"
    ]

    # ------------------------------------------
    # Timestamps
    # ------------------------------------------

    if pd.isna(last_stock_movement):

        created_at = product[
            "created_at"
        ]

    else:

        created_at = last_stock_movement

    updated_at = created_at

    # ------------------------------------------
    # Build Inventory Record
    # ------------------------------------------

    inventory = {

        "inventory_id":
            inventory_id,

        "product_id":
            product["product_id"],

        "warehouse_id":
            product["warehouse_id"],

        "current_stock":
            current_stock,

        "reserved_stock":
            reserved_stock,

        "available_stock":
            available_stock,

        "inventory_status":
            inventory_status,

        "last_stock_movement":
            last_stock_movement,

        "created_at":
            created_at,

        "updated_at":
            updated_at

    }

    return inventory

def generate_inventory():
    """
    Generates the inventory snapshot
    for every active product.
    """

    print()

    print(
        "Generating inventory..."
    )

    # ------------------------------------------
    # Load Reference Data
    # ------------------------------------------

    reference_data = (
        load_inventory_reference_data()
    )

    products_df = (
        reference_data["products"]
    )

    orders_df = (
        reference_data["orders"]
    )

    order_details_df = (
        reference_data["order_details"]
    )

    # ------------------------------------------
    # Warehouse Assignment
    # ------------------------------------------

    products_df = assign_product_warehouse(
        products_df
    )

    # ------------------------------------------
    # Sales Summary
    # ------------------------------------------

    inventory_products = (
        summarize_product_sales(

            products_df,

            orders_df,

            order_details_df

        )
    )

    # ------------------------------------------
    # Build Inventory Records
    # ------------------------------------------

    inventory_records = []

    inventory_counter = 1

    for _, product in (
        inventory_products.iterrows()
    ):

        inventory = (
            build_inventory_record(

                f"INV{inventory_counter:04d}",

                product

            )
        )

        inventory_records.append(
            inventory
        )

        inventory_counter += 1

    # ------------------------------------------
    # DataFrame
    # ------------------------------------------

    inventory_df = pd.DataFrame(
        inventory_records
    )

    # ------------------------------------------
    # Validation
    # ------------------------------------------

    validate_inventory(

        inventory_df,

        inventory_products

    )

    # ------------------------------------------
    # Save
    # ------------------------------------------

    save_csv(

        inventory_df,

        "inventory.csv"

    )

    print(

        f"✓ {len(inventory_df)} inventory records generated."

    )

    print(
        "✓ inventory.csv saved."
    )

    return inventory_df

def validate_inventory_ids(
    inventory_df
):
    """
    Ensures Inventory IDs are unique.
    """

    if inventory_df[
        "inventory_id"
    ].duplicated().any():

        raise ValueError(
            "Duplicate inventory IDs found."
        )

    print(
        "✓ Inventory IDs are unique"
    )

def validate_inventory_product_references(
    inventory_df,
    products_df
):
    """
    Ensures every product exists.
    """

    valid_products = set(
        products_df["product_id"]
    )

    invalid = inventory_df[
        ~inventory_df["product_id"].isin(
            valid_products
        )
    ]

    if not invalid.empty:

        raise ValueError(
            "Invalid product reference found."
        )

    print(
        "✓ Product references are valid"
    )

def validate_inventory_warehouse_references(
    inventory_df
):
    """
    Ensures warehouse IDs are valid.
    """

    valid = {

        "WH001",
        "WH002",
        "WH003"

    }

    if not inventory_df[
        "warehouse_id"
    ].isin(valid).all():

        raise ValueError(
            "Invalid warehouse ID found."
        )

    print(
        "✓ Warehouse references are valid"
    )

def validate_stock_quantities(
    inventory_df
):
    """
    Validates stock quantities.
    """

    if (
        inventory_df[
            "current_stock"
        ] < 0
    ).any():

        raise ValueError(
            "Negative current stock found."
        )

    if (
        inventory_df[
            "reserved_stock"
        ] < 0
    ).any():

        raise ValueError(
            "Negative reserved stock found."
        )

    if (
        inventory_df[
            "available_stock"
        ] < 0
    ).any():

        raise ValueError(
            "Negative available stock found."
        )

    expected = (

        inventory_df[
            "current_stock"
        ]

        -

        inventory_df[
            "reserved_stock"
        ]

    )

    if not expected.equals(

        inventory_df[
            "available_stock"
        ]

    ):

        raise ValueError(
            "Available stock validation failed."
        )

    print(
        "✓ Stock quantities validated"
    )

def validate_inventory_status(
    inventory_df
):
    """
    Validates inventory status values.
    """

    valid = {

        "In Stock",
        "Low Stock",
        "Out of Stock"

    }

    if not inventory_df[
        "inventory_status"
    ].isin(valid).all():

        raise ValueError(
            "Invalid inventory status found."
        )

    print(
        "✓ Inventory status validated"
    )

def validate_last_stock_movement(
    inventory_df
):
    """
    Ensures movement dates
    are not in the future.
    """

    dates = pd.to_datetime(

        inventory_df[
            "last_stock_movement"
        ]

    )

    if (
        dates
        > DATASET_END_DATE
    ).any():

        raise ValueError(
            "Future stock movement found."
        )

    print(
        "✓ Stock movement dates validated"
    )

def validate_inventory_timestamps(
    inventory_df
):
    """
    Validates timestamps.
    """

    created = pd.to_datetime(

        inventory_df[
            "created_at"
        ]

    )

    updated = pd.to_datetime(

        inventory_df[
            "updated_at"
        ]

    )

    if (
        updated < created
    ).any():

        raise ValueError(
            "Inventory timestamps invalid."
        )

    print(
        "✓ Timestamp validation passed"
    )

def validate_one_inventory_per_product(
    inventory_df
):
    """
    Ensures one inventory row
    exists per product.
    """

    if inventory_df[
        "product_id"
    ].duplicated().any():

        raise ValueError(
            "Duplicate inventory product found."
        )

    print(
        "✓ One inventory record per product"
    )

def validate_inventory_business_rules(
    inventory_df,
    products_df
):
    """
    Validates inventory status
    against stock levels and
    reorder levels.
    """

    validation_df = (
        inventory_df.merge(

            products_df[
                [
                    "product_id",
                    "reorder_level"
                ]
            ],

            on="product_id",

            how="left"

        )
    )

    for _, row in validation_df.iterrows():

        available_stock = row[
            "available_stock"
        ]

        reorder_level = row[
            "reorder_level"
        ]

        actual_status = row[
            "inventory_status"
        ]

        if available_stock == 0:

            expected_status = (
                "Out of Stock"
            )

        elif (
            available_stock
            <= reorder_level
        ):

            expected_status = (
                "Low Stock"
            )

        else:

            expected_status = (
                "In Stock"
            )

        if (
            actual_status
            != expected_status
        ):

            raise ValueError(

                "Inventory status business rule failed. "

                f"Product: {row['product_id']} | "

                f"Expected: {expected_status} | "

                f"Actual: {actual_status}"

            )

    print(
        "✓ Inventory business rules validated"
    )

def validate_inventory(
    inventory_df,
    products_df
):
    """
    Runs all inventory validations.
    """

    print()

    print(
        "Running inventory validations..."
    )

    validate_inventory_ids(
        inventory_df
    )

    validate_inventory_product_references(
        inventory_df,
        products_df
    )

    validate_inventory_warehouse_references(
        inventory_df
    )

    validate_stock_quantities(
        inventory_df
    )

    validate_inventory_status(
        inventory_df
    )

    validate_inventory_business_rules(
    inventory_df,
    products_df
)

    validate_last_stock_movement(
        inventory_df
    )

    validate_inventory_timestamps(
        inventory_df
    )

    validate_one_inventory_per_product(
        inventory_df
    )

    print()

    print(
        "ALL INVENTORY VALIDATIONS PASSED"
    )


# ------------------------------------------------------
# Main
# ------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("LOTS Corp. Dataset Generator")
    print(lots_corp_version)
    print("=" * 60)

    # ==================================================
    # Supplier Master
    # ==================================================

    suppliers_df = generate_suppliers()

    save_csv(
        suppliers_df,
        "suppliers.csv"
    )

    # ==================================================
    # Product Master
    # ==================================================

    summarize_product_catalog()

    products_df = generate_products(
        suppliers_df
    )

    validate_products(
        products_df,
        suppliers_df
    )

    # ==================================================
    # Customer Master
    # ==================================================

    customers_df = generate_customers()

    validate_customers(
        customers_df
    )

    # ==================================================
    # Employee Master
    # ==================================================

    employees_df = generate_employees()

    # ==================================================
    # Generation Summary
    # ==================================================

    print()
    print("=" * 60)
    print("Generation Summary")
    print("=" * 60)

    print(
        f"Suppliers : {len(suppliers_df)}"
    )

    print(
        f"Products  : {len(products_df)}"
    )

    print(
        f"Customers : {len(customers_df)}"
    )

    print(
        f"Employees : {len(employees_df)}"
    )

    print("=" * 60)

    print()
    print("Supplier Preview")
    print(suppliers_df.head())

    print()
    print("Customer Preview")
    print(customers_df.head())

    print()
    print("Employee Preview")
    print(employees_df.head())

    print()
    print("LOTS Corp. Master Data Generation Complete.")

    # ==================================================
    # Orders
    # ==================================================

    orders_df = generate_orders(
        load_order_reference_data()
    )

    # ==================================================
    # Orders Details
    # ==================================================

    order_details_df = generate_order_details()

    # ==================================================
    # Inventory
    # ==================================================

    inventory_df = generate_inventory()
