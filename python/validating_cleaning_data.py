import pandas as pd

file1 = "customers.csv"                 #---------------------------------------------------------------
file2 = "cleaned_customers.csv"         # CSV files needed 
file3 = "employees.csv"                 #---------------------------------------------------------------
file4 = "cleaned_employees.csv"
file5 = "products.csv"
file6 = "cleaned_products.csv"
file7 = "suppliers.csv"
file8 = "cleaned_suppliers.csv"

original_customer_df = pd.read_csv(file1, encoding="cp1252")    #---------------------------------------------------------------
cleaned_customer_df = pd.read_csv(file2, encoding="cp1252")     # Reading the CSV files using pandas read_csv() function. 
original_employee_df = pd.read_csv(file3)                       #
cleaned_employee_df = pd.read_csv(file4)                        #
original_product_df = pd.read_csv(file5)                        #
cleaned_product_df = pd.read_csv(file6)                         #
original_supplier_df = pd.read_csv(file7)                       #
cleaned_supplier_df = pd.read_csv(file8)                        #---------------------------------------------------------------

print()
if original_customer_df.equals(cleaned_customer_df):                #---------------------------------------------------------------
    print(f"The {file1} and {file2} contain Identical data.")       # Comparing if the two CSV files are equal, this is to validate
else:                                                               # that the cleaning is effective
    print(f"The {file1} and {file2} are different")                 #
if original_employee_df.equals(cleaned_employee_df):                #
    print(f"The {file3} and {file4} contain Identical data.")       #
else:                                                               #
    print(f"The {file3} and {file4} are different")                 #
if original_product_df.equals(cleaned_product_df):                  #
    print(f"The {file5} and {file6} contain Identical data.")       #
else:                                                               #
    print(f"The {file5} and {file6} are different")                 #
if original_supplier_df.equals(cleaned_supplier_df):                #
    print(f"The {file7} and {file8} contain Identical data.")       #
else:                                                               #
    print(f"The {file7} and {file8} are different")                 #---------------------------------------------------------------   
print()             

print(original_customer_df.compare(cleaned_customer_df))        #---------------------------------------------------------------
print(original_employee_df.compare(cleaned_employee_df))        # This will compare the two CSVs difference 
print(original_product_df.compare(cleaned_product_df))          #
print(original_supplier_df.compare(cleaned_supplier_df))        #---------------------------------------------------------------

