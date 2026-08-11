"""
============================================================
LOTS Corp. Data Quality Injector
Version 1.0
============================================================

Purpose
-------
Creates realistic data quality issues from the validated
LOTS Corp. synthetic ERP dataset.

The original dataset remains untouched.

Source:
    data/raw/

Output:
    data/messy/

Author:
    Jopet Pascual

============================================================
"""

from pathlib import Path

from datetime import datetime

import random

import pandas as pd

import math

# ======================================================
# Random Seed
# ======================================================

RANDOM_SEED = 42

random.seed(
    RANDOM_SEED
)

# ======================================================
# Project Paths
# ======================================================

PROJECT_DIR = (
    # Path(__file__).resolve().parent.parent
    Path(__file__).parent
)

DATA_DIR = (
    PROJECT_DIR / "data"
)

RAW_DIR = (
    DATA_DIR / "raw"
)

MESSY_DIR = (
    DATA_DIR / "messy"
)

MESSY_DIR.mkdir(

    parents=True,

    exist_ok=True

)

# ------------------------------------------
# Text Quality Injection Rate
# ------------------------------------------

TEXT_QUALITY_RATE = 0.05

# ======================================================
# Enable Data Quality Issues
# ======================================================

ENABLE_LEADING_SPACES = True

ENABLE_TRAILING_SPACES = True

ENABLE_DOUBLE_SPACES = True

ENABLE_UPPERCASE = True

ENABLE_LOWERCASE = True

ENABLE_TYPOS = True

ENABLE_BLANK_VALUES = True

ENABLE_RANDOM_CASE = True

COLUMN_TEXT_QUALITY_ISSUES = {

    "default": [

        "leading_space",

        "trailing_space",

        "double_space",

        "uppercase",

        "lowercase",

        "random_case",

        "typo"

    ],

    "email": [

        "leading_space",

        "trailing_space",

        "uppercase",

        "lowercase"

    ],

    "camel case name": [
    
            "leading_space",
    
            "trailing_space",

            "double_space"
    
        ]

}

# ======================================================
# Dataset Files
# ======================================================

DATASET_FILES = {

    "suppliers":
        "suppliers.csv",

    "products":
        "products.csv",

    "customers":
        "customers.csv",

    "employees":
        "employees.csv",

    "orders":
        "orders.csv",

    "order_details":
        "order_details.csv",

    "inventory":
        "inventory.csv"

}

def choose_random_indices(
    dataframe,
    rate
):
    """
    Randomly selects row indices based
    on the specified injection rate.
    """

    number_of_rows = len(
        dataframe
    )

    number_to_modify = math.ceil(
        number_of_rows * rate
    )

    if number_to_modify == 0:

        return []

    return random.sample(

        list(dataframe.index),

        number_to_modify

    )

def create_typo(
    text
):
    """
    Introduces one realistic typo
    into a text value.
    """

    text = str(text)

    if len(text) < 4:

        return text

    operation = random.choice(

        [

            "swap",

            "remove",

            "duplicate"

        ]

    )

    position = random.randint(

        1,

        len(text) - 2

    )

    if operation == "swap":

        characters = list(text)

        characters[position], characters[position + 1] = (

            characters[position + 1],

            characters[position]

        )

        return "".join(characters)

    elif operation == "remove":

        return (

            text[:position]

            +

            text[position + 1:]

        )

    else:

        return (

            text[:position]

            +

            text[position]

            +

            text[position:]

        )

def create_random_case(
    text
):
    """
    Randomly changes the case
    of alphabetic characters.
    """

    text = str(text)

    characters = []

    for character in text:

        if character.isalpha():

            if random.random() < 0.50:

                characters.append(
                    character.upper()
                )

            else:

                characters.append(
                    character.lower()
                )

        else:

            characters.append(
                character
            )

    return "".join(
        characters
    )

def create_leading_space(
    value
):
    """
    Adds one leading space.
    """

    if pd.isna(value):

        return value

    return " " + str(value)

def create_trailing_space(
    value
):
    """
    Adds one trailing space.
    """

    if pd.isna(value):

        return value

    return str(value) + " "

def create_uppercase(
    value
):
    """
    Converts text to uppercase.
    """

    if pd.isna(value):

        return value

    return str(value).upper()

def create_lowercase(
    value
):
    """
    Converts text to lowercase.
    """

    if pd.isna(value):

        return value

    return str(value).lower()

def create_double_space(
    value
):
    """
    Replaces the first single
    space with a double space.
    """

    if pd.isna(value):

        return value

    value = str(value)

    if " " not in value:

        return value

    return value.replace(
        " ",
        "  ",
        1
    )

TEXT_TRANSFORMERS = {

    "leading_space":
        create_leading_space,

    "trailing_space":
        create_trailing_space,

    "double_space":
        create_double_space,

    "uppercase":
        create_uppercase,

    "lowercase":
        create_lowercase,

    "random_case":
        create_random_case,

    "typo":
        create_typo

}

def inject_blank_values(
    dataframe,
    column_name,
    rate
):
    """
    Replaces randomly selected
    values with missing values.
    """

    indices = choose_random_indices(

        dataframe,

        rate

    )

    modified = 0

    for index in indices:

        dataframe.at[
            index,
            column_name
        ] = pd.NA

        modified += 1

    return modified

def load_dataset(dataset_name):
    f"""
    Loads the validated
    {dataset_name} dataset.
    """

    return pd.read_csv(

        RAW_DIR /

        DATASET_FILES[dataset_name]

    )

def save_messy_dataset(
    dataframe,
    filename
):
    """
    Saves a messy dataset.
    """

    dataframe.to_csv(

        MESSY_DIR / filename,

        index=False

    )

    print(

        f"✓ {filename} saved."

    )

def get_active_text_issues():
    """
    Returns every enabled
    text quality issue.
    """

    issues = []

    if ENABLE_LEADING_SPACES:
        issues.append(
            "leading_space"
        )

    if ENABLE_TRAILING_SPACES:
        issues.append(
            "trailing_space"
        )

    if ENABLE_DOUBLE_SPACES:
        issues.append(
            "double_space"
        )

    if ENABLE_UPPERCASE:
        issues.append(
            "uppercase"
        )

    if ENABLE_LOWERCASE:
        issues.append(
            "lowercase"
        )

    if ENABLE_RANDOM_CASE:
        issues.append(
            "random_case"
        )

    if ENABLE_TYPOS:
        issues.append(
            "typo"
        )

    return issues

def inject_text_quality_issues(
    dataframe,
    text_columns
):
    """
    Injects one random text quality
    issue per selected cell.
    """

    labels = {

        "leading_space":
            "Leading Spaces",

        "trailing_space":
            "Trailing Spaces",

        "double_space":
            "Double Spaces",

        "uppercase":
            "Uppercase",

        "lowercase":
            "Lowercase",

        "random_case":
            "Random Case",

        "typo":
            "Typos"

    }

    for column in text_columns:

        if column not in dataframe.columns:

            raise KeyError(

                f"Column '{column}' does not exist."

            )

        if "email" in column.lower():
            profile = ("email")

        elif dataframe[column].str.contains(
                        "[A-Z][a-z]+[A-Z]+[a-z]*",
                        regex=True,
                        na=False
                    ).to_list().count(True)/ len(dataframe[column]) > 0.3:
            profile = ("camel case name")
        
        else:
            profile = ("default")

        active_issues = [

            issue

            for issue in COLUMN_TEXT_QUALITY_ISSUES[
                profile
            ]

            if issue in get_active_text_issues()

        ]

        if not active_issues:

            continue

        print()

        print(column)

        print("-" * 40)

        indices = choose_random_indices(

            dataframe,

            TEXT_QUALITY_RATE

        )

        summary = {

            issue: 0

            for issue in active_issues

        }

        for index in indices:

            value = dataframe.at[
                index,
                column
            ]

            if pd.isna(value):

                continue

            issue = random.choice(

                active_issues

            )

            transformer = TEXT_TRANSFORMERS[
                issue
            ]

            new_value = transformer(

                value

            )

            if new_value == value:

                continue

            dataframe.at[
                index,
                column
            ] = new_value

            summary[
                issue
            ] += 1

        for issue in active_issues:

            print(

                f"{labels[issue]:16}: "

                f"{summary[issue]}"

            )

def inject_dataset_text_quality_issues(
        dataframe,
        dataset_name,
        filename,
        text_columns
):
    f"""
    Injects realistic text quality
    issues into {filename}.
    """

    print()

    print("=" * 60)
    print(
        f"Injecting {dataset_name} Data Quality Issues"
    )
    print("=" * 60)
    inject_text_quality_issues(

        dataframe,

        text_columns

    )

    print()

    save_messy_dataset(

        dataframe,

        DATASET_FILES[f"{filename[:-4]}"]

    )

    return dataframe


pattern = "[A-Z][a-z]+[A-Z]+[a-z]*"

#------------------------------------------------------------
# Target datasets to be injected are the following:
# suppliers.csv
# products.csv
# customers.csv
# employees.csv
#------------------------------------------------------------


#------------------------------------------------------------
# Load the original datasets
#------------------------------------------------------------

suppliers_df = load_dataset("suppliers")
customers_df = load_dataset("customers")
products_df = load_dataset("products")
employees_df = load_dataset("employees")

#------------------------------------------------------------
# Create text columns of each dataset to be injected 
# of text quality issues
#------------------------------------------------------------

suppliers_text_columns = [
    col for col in suppliers_df.columns 
        if [not str(suppliers_df[col].iloc[i]).endswith(
            ("0","1","2","3","4","5","6","7","8","9", "True", "False", "TRUE", "FALSE")
        ) for i in range(len(suppliers_df[col]))].count(True)/len(suppliers_df[col]) > 0.5
]

customers_text_columns = [
    col for col in customers_df.columns 
        if [not str(customers_df[col].iloc[i]).endswith(
            ("0","1","2","3","4","5","6","7","8","9", "True", "False", "TRUE", "FALSE")
        ) for i in range(len(customers_df[col]))].count(True)/len(customers_df[col]) > 0.5
]

products_text_columns = [
    col for col in products_df.columns 
        if [not str(products_df[col].iloc[i]).endswith(
            ("0","1","2","3","4","5","6","7","8","9", "True", "False", "TRUE", "FALSE")
        ) for i in range(len(products_df[col]))].count(True)/len(products_df[col]) > 0.5
]

employees_text_columns = [
    col for col in employees_df.columns 
        if [not str(employees_df[col].iloc[i]).endswith(
            ("0","1","2","3","4","5","6","7","8","9", "True", "False", "TRUE", "FALSE")
        ) for i in range(len(employees_df[col]))].count(True)/len(employees_df[col]) > 0.5
]

#------------------------------------------------------------
# Start injecting the datasets column choices and then save
# to messy/ folder the injected datasets
#------------------------------------------------------------

print("=" * 60)
print("Suppliers text columns: ", suppliers_text_columns)
print("=" * 60)
print()

inject_dataset_text_quality_issues(
    dataframe=suppliers_df,
    dataset_name="Suppliers",
    filename="suppliers.csv",
    text_columns=suppliers_text_columns
)

print("=" * 60)
print("Customers text columns: ", customers_text_columns)
print("=" * 60)
print()

inject_dataset_text_quality_issues(
    dataframe=customers_df,
    dataset_name="Customers",
    filename="customers.csv",
    text_columns=customers_text_columns
)

print("=" * 60)
print("Products text columns: ", products_text_columns)
print("=" * 60)
print()

inject_dataset_text_quality_issues(
    dataframe=products_df,
    dataset_name="Products",
    filename="products.csv",
    text_columns=products_text_columns
)

print("=" * 60)
print("Employees text columns: ", employees_text_columns)
print("=" * 60)
print()

inject_dataset_text_quality_issues(
    dataframe=employees_df,
    dataset_name="Employees",
    filename="employees.csv",
    text_columns=employees_text_columns
)
