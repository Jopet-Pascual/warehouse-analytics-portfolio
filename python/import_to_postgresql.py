from pathlib import Path

import pandas as pd
import psycopg2
import io

DB_CONFIG = {
    "host": "localhost",
    "port": "my_port", # Replaced the "my_port" with your port as numeric not string text
    "dbname": "lotscorp_warehouse",
    "user": "postgres",
    "password": "********" # Replaced the askterisk with your password
}

CLEANED_DATA_DIR = (
    Path(__file__)
    .resolve()
    .parent.parent
    /"data"
    /"cleaned"
)

IMPORT_ORDER = [

    ["cleaned_suppliers", "suppliers"],

    ["cleaned_products", "products"],

    ["cleaned_customers", "customers"],

    ["cleaned_employees", "employees"],

    ["orders", "orders"],

    ["inventory", "inventory"],

    ["order_details", "order_details"]

]

cleaned_CSVs = [

    "cleaned_suppliers",

    "cleaned_products",

    "cleaned_customers",

    "cleaned_employees",

    "order",

    "inventory",

    "order_details"
]

def connect_database():
    """
    Connect to the PostgreSQL database.
    """

    return psycopg2.connect(

        **DB_CONFIG

    )

def read_csv(csv_filename):
    """
    Read a cleaned CSV file into a pandas DataFrame.
    """

    csv_path = (
        CLEANED_DATA_DIR
        / f"{csv_filename}.csv"
    )

    return pd.read_csv(csv_path)


def import_table(
    connection,
    csv_filename,
    table_name
):
    """
    Import one cleaned CSV into PostgreSQL.
    """

    dataframe = read_csv(
        csv_filename
    )

    buffer = io.StringIO()

    dataframe.to_csv(

        buffer,

        index=False,

        header=False

    )

    buffer.seek(0)

    cursor = connection.cursor()

    cursor.copy_expert(

        sql=f"""
        COPY {table_name}
        FROM STDIN
        WITH (
            FORMAT CSV
        )
        """,

        file=buffer

    )

    connection.commit()

    print(

        f"✓ {csv_filename}.csv"

    )

    print(

        f"Rows Imported : {len(dataframe):,}"

    )

    print()

def main():

    print("=" * 60)

    print(

        "Importing Cleaned CSV Files into PostgreSQL"

    )

    print("=" * 60)

    print()

    connection = connect_database()

    for name in IMPORT_ORDER:
        import_table(
            connection,
            csv_filename=name[0],
            table_name=name[1])

    connection.close()

    print("=" * 60)

    print(

        "Database Import Complete"

    )

    print("=" * 60)


if __name__ == "__main__":

    main()

