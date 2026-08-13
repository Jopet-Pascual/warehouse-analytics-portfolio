# Excel Skills
This directory contains all Excel files used to cleaning the data for LOTS Corp Warehouse Analytics project.

---

## Data Cleaning using Power Query

Data Cleaning Workflow:

1. Importing the data

![Data tab](/images/power_query_editor_screenshots/excel_getdata_fromfile_folder.png)

![Data tab](/images/power_query_editor_screenshots/excel_load_transform.png)

![Data tab](/images/power_query_editor_screenshots/excel_powerquery_editor.png)

![Data tab](/images/power_query_editor_screenshots/excel_PreviewOf_customerCSV.png)

2. Transforming columns

![power query editor](/images/power_query_editor_screenshots/excel_AppliedTrimTo_customer_id.png)

3. Creating Reusable Custom Functions

![Creating Reusable Custom Functions](/images/power_query_editor_screenshots/excel_AddBlankQueryForReusableFunction.png)

![Creating Reusable Custom Functions](/images/power_query_editor_screenshots/excel_CreatingCleanTextFunctionWithExplanation.png)

![Creating Reusable Custom Functions](/images/power_query_editor_screenshots/excel_RenamingBlankQuery.png)

![Creating Reusable Custom Functions](/images/power_query_editor_screenshots/excel_InvokeCleanTextTo_industry.png)

![Creating Reusable Custom Functions](/images/power_query_editor_screenshots/excel_Removing_industry.png)

4. Creating Reference Column

    I created reference queries for the columns and transformed them by removing duplicates and sorting the values in accending order. This produced a list of unique values, making it easier to identify data type errors and inconsistent entries. After reviewing the unique values, I corrected the errors by replacing the incorrect values with the appropriate ones.

![Creating Reference Column](/images/power_query_editor_screenshots/excel_CreateReferenceQueryFor_cleaned_region.png)

![Creating Reference Column](/images/power_query_editor_screenshots/excel_RenameReferenceQuery_cleaned_region.png)

![Creating Reference Column](/images/power_query_editor_screenshots/excel_RemoveAllColumnsExcept_cleaned_region.png)

![Creating Reference Column](/images/power_query_editor_screenshots/excel_QueryReference_RemoveDuplicates_cleaned_region.png)

![Creating Reference Column](/images/power_query_editor_screenshots/excel_ReferenceQuery_ResultOfRemovesDuplicates_cleaned_region.png)

![Creating Reference Column](/images/power_query_editor_screenshots/excel_ReferenceQuery_CopyOneValueInUniqueColumn.png)

![Creating Reference Column](/images/power_query_editor_screenshots/excel_ReplaceValues_cleaned_region.png)

![Creating Reference Column](/images/power_query_editor_screenshots/excel_ReferenceQuery_AutomaticUpdateUniqueValue_AfterReplaceValue.png)

![Creating Reference Column](/images/power_query_editor_screenshots/excel_UniqueRegionCleaned.png)

5. Cleaned datasets

    - Customer Dataset

    ![Customer Dataset](/images/power_query_editor_screenshots/excel_DataCleaningCustomersDone.png)

    Exported CSV file: [cleaned_customers.csv](/data/cleaned/cleaned_customers.csv)


    - Employee Dataset

    ![Employee Dataset](/images/power_query_editor_screenshots/excel_DataCleaningEmployeesDone.png)

    Exported CSV file: [cleaned_employees.csv](/data/cleaned/cleaned_employees.csv)

    - Product Dataset

    ![Product Dataset](/images/power_query_editor_screenshots/excel_DataCleaningProductsDone.png)

    Exported CSV file: [cleaned_products.csv](/data/cleaned/cleaned_products.csv)

    - Supplier Dataset

    ![Supplier Dataset](/images/power_query_editor_screenshots/excel_DataCleaningSuppliersDone.png)

    Exported CSV file: [cleaned_suppliers.csv](/data/cleaned/cleaned_suppliers.csv)

    To see the Excel file used to clean the datasets click --> [data_cleaning_version2.xlsx](data_cleaning_version2.xlsx)

    ###### Back to --> [main README-Skills Demonstrated](/README.md#documentation)
