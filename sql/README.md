# SQL Scripts

This directory contains all SQL scripts used to build, validate, and analyze the PostgreSQL database for the LOTS Corp Warehouse Analytics project.

The scripts are organized in the order they should be executed, from database creation through business analysis.

---

## Files

| File                        | Description                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| [01_create_database.sql](01_create_database.sql)    | Creates the PostgreSQL database.                                                           |
| [02_create_tables.sql](02_create_tables.sql)      | Creates all database tables, primary keys, foreign keys, and constraints.                  |
| [import_to_postgresql.py](/python/import_to_postgresql.py)         | Creates Python script that can run to import the validated CSV datasets into PostgreSQL.             |
| [03_verify_data.sql](03_verify_data.sql) | Contains SQL queries used to validate the imported data and verify database integrity.     |
| [04_analytical_queries.sql](04_analytical_queries.sql)   | Contains business analysis queries used to answer warehouse and sales reporting questions. |

---

## Execution Order

Execute the SQL scripts in the following order:

1. Create the PostgreSQL database.
![Create lotscorp_database](/images/postgre_screenshots/postgre_CreatingDataBase_lotscorp_warehouse.png)
2. Create all database tables.

    Example Code:
    ![Create Suppliers Table](/images/postgre_screenshots/postgre_CreatingSuppliersTable.png)
    To see the full code: [02_create_tables.sql](/sql/02_create_tables.sql)
    
    ###### [back to main README](/README.md#skills-demonstrated)

3. Import the validated CSV datasets.

    Example Code:

    ![Import order_details.csv to lotscorp_warehouse db](/images/python-importing_dataset_to_dbTable_screenshots/python_ImportingCleanedOrderDetailsToPostgreSQLdb_lotscorp_warehouse.png)

    Output:

    ![import_to_postgresql.py Output](/images/python-importing_dataset_to_dbTable_screenshots/python_ImportingCleanedOrderDetailsToPostgreSQLdb_lotscorp_warehouse_Output.png)
4. Validate the imported data.

    ##### Verify Using Queries
    ```text 
    Verify Row Counts
    ```

    suppliers table

    ![suppliers table](/images/postgre_screenshots/postgre_Verified_Suppliers.png)

    products table

    ![products table](/images/postgre_screenshots/postgre_Verified_Products.png)

    customers table

    ![customers table](/images/postgre_screenshots/postgre_Verified_Customers.png)

    employees table

    ![employees table](/images/postgre_screenshots/postgre_Verified_Employees.png)

    orders table

    ![orders table](/images/postgre_screenshots/postgre_Verified_Orders.png)

    inventory table

    ![inventory table](/images/postgre_screenshots/postgre_Verified_Inventory.png)

    order_details table

    ![order_details table](/images/postgre_screenshots/postgre_Verified_OrderDetails.png)

    ```text
    Verifying Foreign Keys
    ```

    Checking Products without Suppliers
    
    ![Checking Products without Suppliers](/images/postgre_screenshots/postgre_VerifyingForeignKeyProducts_ProductsWithoutSuppliers.png)

    Orders without Customers

    ![Orders without Customers](/images/postgre_screenshots/postgre_VerifyingForeignKeyOrders_OrdersWithoutCustomers.png)

    Orders without Sales Representatives

    ![Orders without Sales Representatives](/images/postgre_screenshots/postgre_VerifyingForeignKeyOrdersSalesRep_OrdersWithoutSalesRepresentatives.png)

    Inventory without Products
    
    ![Inventory without Products](/images/postgre_screenshots/postgre_VerifyingForeignKeyInventoryProductID_InventoryWithoutProducts.png)

    Order Details without Orders
    
    ![Order Details without Orders](/images/postgre_screenshots/postgre_VerifyingForeignKeyOrderDetailsOrderID_OrderDetailsWithoutOrders.png)

    Order Details without Products
    
    ![Order Details without Products](/images/postgre_screenshots/postgre_VerifyingForeignKeyOrderDetailsProductID_OrderDetailsWithoutProducts.png)

    ```text
    Verifying Primary Keys 
    ```

    supplier_id

    ![supplier_id](/images/postgre_screenshots/postgre_VerifiedSuppliersNoDuplicatePrimaryKey.png)

    product_id

    ![product_id](/images/postgre_screenshots/postgre_VerifiedProductsNoDuplicatePrimaryKey.png)

    customer_id

    ![customer_id](/images/postgre_screenshots/postgre_VerifiedCutomersNoDuplicatePrimaryKey.png)

    employee_id

    ![employee_id](/images/postgre_screenshots/postgre_VerifiedEmployeesNoDuplicatePrimaryKey.png)

    order_id

    ![order_id](/images/postgre_screenshots/postgre_VerifiedOrdersNoDuplicatePrimaryKey.png)

    inventory_id

    ![inventory_id](/images/postgre_screenshots/postgre_VerifiedInventoryNoDuplicatePrimaryKey.png)

    order_detail_id

    ![order_detail_id](/images/postgre_screenshots/postgre_VerifiedOrderDetailsNoDuplicatePrimaryKey.png)

    ###### Back to --> [main README - Skills Demontrated](/README.md#skills-demonstrated)

5. Execute the business analysis queries.

    ### Sales KPIs

    #### Total Revenue

    ![Total Revenue](/images/postgre_screenshots/postgre_REVENUE.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Total Profit

    ![Total Profit](/images/postgre_screenshots/postgre_TOTAL_PROFIT.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Total Orders

    ![Total Orders](/images/postgre_screenshots/postgre_TOTAL_ORDERS.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Total Cancelled Orders

    ![Total Cancelled Orders](/images/postgre_screenshots/postgre_TOTAL_CANCELLED_ORDERS.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Total Returned Orders

    ![Total Returned Orders](/images/postgre_screenshots/postgre_TOTAL_RETURNED_ORDERS.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Average Order Value

    ![Average Order Value](/images/postgre_screenshots/postgre_AVERAGE_ORDER_VALUE.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Annual Sales Revenue

    ![Annual Sales Revenue](/images/postgre_screenshots/postgre_AnnualSalesRevenue.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Monthly Sales Trend

    ![Monthly Sales Trend](/images/postgre_screenshots/postgre_MonthlySalesTrend.png)

    Result:
    
    |sales_month|total_sales|
    |:----------:|:----------:|
    |2024-01-01 00:00:00+08|450664729.39|
    |2024-02-01 00:00:00+08|307973821.42|
    |2024-03-01 00:00:00+08|320572690.43|
    |2024-04-01 00:00:00+08|213815986.82|
    |2024-05-01 00:00:00+08|361863429.87|
    |2024-06-01 00:00:00+08|494136241.39|
    |2024-07-01 00:00:00+08|369606182.19|
    |2024-08-01 00:00:00+08|400778102.96|
    |2024-09-01 00:00:00+08|469807943.87|
    |2024-10-01 00:00:00+08|534431462.60|
    |2024-11-01 00:00:00+08|784085700.49|
    |2024-12-01 00:00:00+08|1013545484.05|
    |2025-01-01 00:00:00+08|1207689358.62|
    |2025-02-01 00:00:00+08|915901172.50|
    |2025-03-01 00:00:00+08|951561855.82|
    |2025-04-01 00:00:00+08|653980930.19|
    |2025-05-01 00:00:00+08|1031486115.66|
    |2025-06-01 00:00:00+08|1494522604.11|
    |2025-07-01 00:00:00+08|1235778979.22|
    |2025-08-01 00:00:00+08|1237297296.65|
    |2025-09-01 00:00:00+08|1550605166.98|
    |2025-10-01 00:00:00+08|1724719159.49|
    |2025-11-01 00:00:00+08|2004316137.02|
    |2025-12-01 00:00:00+08|2559866404.79|
    |2026-01-01 00:00:00+08|2302007627.53|
    |2026-02-01 00:00:00+08|1563220019.33|
    |2026-03-01 00:00:00+08|1547549986.21|
    |2026-04-01 00:00:00+08|964826552.49|
    |2026-05-01 00:00:00+08|1555316746.68|
    |2026-06-01 00:00:00+08|2163705136.14|
    |2026-07-01 00:00:00+08|1162953114.53|


    Click to view the result --> [monthly_sales_trend_result.csv](monthly_sales_trend_result.csv)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Sales by Order Source

    ![Sales by Order Source](/images/postgre_screenshots/postgre_SalesByOrderSource.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Orders by Status

    ![Orders by Status](/images/postgre_screenshots/postgre_OrdersByStatus.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Payment Status Distribution

    ![Payment Status Distribution](/images/postgre_screenshots/postgre_PaymentStatusDistribution.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    #### Average Order Value by Order Source

    ![Average Order Value by Order Source](/images/postgre_screenshots/postgre_AverageOrderValueByOrderSource.png)

    [Back to previous](/README.md#executive-sales-dashboard)

    ### Customer KPIs

    #### Top 10 Customers by Sales Revenue

    ![Top 10 Customers by Sales Revenue](/images/postgre_screenshots/postgre_Top10CustomersBySalesRevenue.png)

    Result:

    |customer_id|customer_name|total_sales|
    |:---------:|:-----------:|:---------:|
    |CUS0183|UnityWood Point State College|481173336.84|
    |CUS0133|BrightForge River Technologies Inc.|474339544.93|
    |CUS0025|GreenHarbor Hill Industrial Corporation|473352834.94|
    |CUS0035|RedHill Gate Municipal Government|471552166.48|
    |CUS0051|FirstWorks Harbor General Hospital|456144708.88|
    |CUS0010|RedHorizon Works Retail Group|446156915.84|
    |CUS0257|WestAxis Peak Commercial Center|431709578.95|
    |CUS0293|EverWorks Works Trading Corporation|431556032.81|
    |CUS0195|NorthLine River Business Solutions|429092050.47|
    |CUS0029|BluePoint Peak State College|424996427.63|

    >**Business Insight**
    >
    >A small group of customers often contributes a significant share of total revenue.
    >
    >These customers may be candidates for priority account management, loyalty programs, or targeted retention strategies. 


    [Back to previous](/README.md#customer-analytics-dashboard)

    #### Sales by Customer Type

    ![Sales by Customer Type](/images/postgre_screenshots/postgre_SalesByCustomerType.png)

    Result:

    |customer_type|total_sales|total_customers|
    |:-----------:|:----------:|:--------------:|
    |Corporate|10360531701.95|101|
    |Retail Business|6787386517.18|57|
    |Education|5524572097.60|44|
    |Government|4147621554.79|32|
    |Manufacturing|3616346223.69|29|
    |Healthcare|3112128044.23|25|

    >**Business Insight**
    >
    >Comparing revenue across customer types helps identify the organization's primary market segment and supports sales strategy.

    [Back to previous](/README.md#customer-analytics-dashboard)

    #### Sales by Industry

    ![Sales by Industry](/images/postgre_screenshots/postgre_SalesByIndustry.png)

    Result:

    |industry|total_sales|
    |:------:|:---------:|
    |Logistics|2703518453.66|
    |Academy|2140355123.63|
    |Engineering|1984502992.21|
    |Consulting|1889690052.18|
    |Accounting Services|1803647735.26|
    |Office Supplies|1687286294.74|
    |Telecommunications|1660328226.95|
    |Electronics|1495840890.22|
    |Food Manufacturing|1469534674.69|
    |Furniture|1411714195.78|
    |Medical Clinic|1365982883.92|
    |College|1359918317.87|
    |National Agency|1327782744.22|
    |Computer Store|1318870605.07|
    |Diagnostic Center|1129192336.04|
    |Training Center|1108775032.30|
    |City Government|1040392279.78|
    |Municipal Government|1004943737.18|
    |University|915523623.80|
    |Packaging|914146204.12|
    |Supermarket|873674531.37|
    |Electronics Manufacturing|782106579.30|
    |Public School District|774502793.61|
    |Hospital|616952824.27|
    |Textile|450558765.58|
    |Information Technology|318844241.69|

    >**Business Insight**
    >
    >High-performing industries represent important market opportunities and may justify additional marketing or sales efforts.

    [Back to previous](/README.md#customer-analytics-dashboard)

    #### Customer Status Distribution

    ![Customer Status Distribution](/images/postgre_screenshots/postgre_CustomerStatusDistribution.png)

    >**Business insight**
    >
    >A growing number of inactive customers may indicate customer churn and could signal the need for retention initiatives.

    [Back to previous](/README.md#customer-analytics-dashboard)

    #### Average Revenue per Customer

    ![Average Revenue per Customer](/images/postgre_screenshots/postgre_AverageRevenuePerCustomer.png)

    >**Business insight**
    >
    >Average customer revenue provides a baseline for evaluating customer value and measuring improvements over time.

    [Back to previous](/README.md#customer-analytics-dashboard)

    #### Top Customers by Number of Orders

    ![Top Customers by Number of Orders](/images/postgre_screenshots/postgre_TopCustomersByNumberOfOrders.png)

    >**Business insight**
    >
    >Customers with frequent purchases may represent long-term relationships even if their individual order values are modest.

    [Back to previous](/README.md#customer-analytics-dashboard)

    ### Product KPIs

    #### Top 10 Products by Sales Revenue

    ![Top 10 Products by Sales Revenue](/images/postgre_screenshots/postgre_Top10ProductsBySalesRevenue.png)

    Result:

    |product_id|product_name|total_sales|
    |:--------:|:----------:|:---------:|
    |PROD0041|NovaBook Ultra 18-inch|3507387340.89|
    |PROD0037|ApexBook Pro 16-inch|3228814836.53|
    |PROD0044|NovaStation Workstation|2856096710.84|
    |PROD0036|ApexBook Pro 14-inch|2683564916.75|
    |PROD0046|ApexStation Compact|2440209807.52|
    |PROD0043|NovaStation Tower|2386478930.65|
    |PROD0039|NovaBook Air 16-inch|2175654290.24|
    |PROD0035|ApexBook Essential 13-inch|1849878056.46|
    |PROD0038|NovaBook Air 14-inch|1799890013.04|
    |PROD0045|ApexStation Pro|1529576167.39|

    >**Business insight**
    >
    >High-revenue products represent the company's best-performing offerings and should receive continued inventory availability and marketing support.

    [Back to previous](/README.md#product-performance-dashboard)

    #### Top 10 Products by Profit

    ![Top 10 Products by Profit](/images/postgre_screenshots/postgre_Top10ProductsByProfit.png)

    Result:

    |product_name|total_profit|
    |:----------|----------:|
    |NovaBook Ultra 18-inch|848411908.71|
    |ApexStation Compact|553763795.44|
    |ApexBook Pro 16-inch|525389986.93|
    |NovaStation Workstation|525076011.64|
    |ApexBook Pro 14-inch|495962757.32|
    |ApexBook Essential 13-inch|425587860.81|
    |NovaStation Tower|367715312.35|
    |ApexStation Pro|357554812.95|
    |NovaStation Mini|352924626.57|
    |NovaBook Air 14-inch|337277807.00|


    >**Business insight**
    >
    >Products with high profitability contribute most to overall business growth and may deserve greater sales focus.

    [Back to previous](/README.md#product-performance-dashboard)
    
    #### Top Selling Products

    ![Top Selling Products](/images/postgre_screenshots/postgre_TopSellingProducts.png)

    Result:

    |product_name|units_sold|
    |:-----------|---------:|
    |FlexWebcam HD|99193|
    |FlexKeyboard Wireless|99116|
    |FlexMouse Wireless|98902|
    |FlexHeadset USB|98865|
    |FlexHeadset Bluetooth|98683|
    |FlexHub 4-Port|98313|
    |FlexKeyboard Wired|98175|
    |FlexMouse Wired|98113|
    |DataVault HDD 2TB|82108|
    |DataVault HDD 1TB|81973|

    >**Business insight**
    >
    >Products with consistently high sales volume require careful inventory planning to reduce the risk of stock shortages.

    [Back to previous](/README.md#product-performance-dashboard)

    #### Sales by Product Category

    ![Sales by Product Category](/images/postgre_screenshots/postgre_SalesByProductCategory.png)

    Result:

    |category|total_sales|
    |:-------|----------:|
    |Laptop|15245189453.91|
    |Desktop|10725593151.15|
    |Storage|1929556488.55|
    |Printer|1561625874.96|
    |Networking|1505898300.01|
    |Monitor|990949114.58|
    |Accessories|810749092.70|
    |Office Equipment|779024663.58|

    >**Business insight**
    >
    >Category-level analysis helps management identify product segments that drive overall company performance.

    [Back to previous](/README.md#product-performance-dashboard)

    #### Profit by Product Category

    ![Profit by Product Category](/images/postgre_screenshots/postgre_ProfitByProductCategory.png)

    Result:

    |category|total_profit|
    |:-------|-----------:|
    |Laptop|2966273806.93|
    |Desktop|2157034558.95|
    |Storage|384817106.29|
    |Networking|321712389.03|
    |Printer|319316496.46|
    |Monitor|216946471.93|
    |Office Equipment|195733109.00|
    |Accessories|180488376.99|

    >**Business insight**
    >
    >High-profit categories may justify additional inverstment, promotions, or product expansion.

    [Back to previous](/README.md#product-performance-dashboard)

    #### Average Discount by Product

    ![Average Discount by Product](/images/postgre_screenshots/postgre_AverageDiscountByProduct.png)

    Result:

    |product_name|average_discount_pct|
    |:-----------|-------------------:|
    |OfficePro Projector Business|5.26|
    |OfficePro Shredder Personal|5.25|
    |NovaStation Workstation|5.16|
    |NovaStation Mini|5.16|
    |ApexBook Essential 13-inch|5.15|
    |FlexKeyboard Wired|5.14|
    |SwiftLink Switch 8-Port|5.14|
    |DataVault FlashDrive 32GB|5.13|
    |ApexBook Pro 14-inch|5.13|
    |NovaBook Air 16-inch|5.13|
    |DataVault FlashDrive 64GB|5.13|
    |SwiftLink Switch 16-Port|5.12|
    |SwiftLink Router AC1200|5.11|
    |OfficePro Laminator A4|5.11|
    |DataVault HDD 4TB|5.11|
    |FlexHeadset USB|5.11|
    |VisionView Pro 32-inch|5.11|
    |FlexKeyboard Wireless|5.11|
    |FlexMouse Wireless|5.11|
    |NovaStation Tower|5.11|
    |ApexStation Pro|5.11|
    |FlexMouse Wired|5.10|
    |FlexHub 4-Port|5.10|
    |NovaBook Ultra 18-inch|5.10|
    |DataVault HDD 1TB|5.09|
    |FlexWebcam HD|5.09|
    |FlexHeadset Bluetooth|5.09|
    |VisionView Essential 27-inch|5.09|
    |CorePrint Laser Color|5.09|
    |OfficePro Document Scanner ADF|5.09|
    |ApexStation Compact|5.09|
    |VisionView Ultra 42-inch|5.08|
    |DataVault SSD 1TB|5.08|
    |DataVault SSD 256GB|5.08|
    |DataVault HDD 2TB|5.07|
    |CorePrint Laser Mono|5.07|
    |SwiftLink Access Point Indoor|5.07|
    |CorePrint Label Industrial|5.07|
    |VisionView Essential 24-inch|5.07|
    |NovaBook Air 14-inch|5.06|
    |SwiftLink Router AX1800|5.04|
    |ApexBook Pro 16-inch|5.03|
    |CorePrint InkJet Color|5.01|
    |OfficePro Binding Machine Comb|5.01|
    |CorePrint Label Standard|4.98|

    >**Business Insight**
    >
    >Products with consistently high discounts may indicate aggressive pricing strategies or lower customer demand.

    [Back to previous](/README.md#product-performance-dashboard)

    ### Employee KPIs

    #### Sales Revenue by Sales Representative

    ![Sales Revenue by Sales Representative](/images/postgre_screenshots/postgre_SalesRevenueBySalesRepresentative.png)

    Result:

    |employee_id|full_name|total_sales|total_orders|
    |:----------|:--------|----------:|-----------:|
    |EMP0004|Paolo De Guzman|8509819043.50|118789|
    |EMP0007|Michael Bautista|8167771578.81|114649|
    |EMP0008|Irene Domingo|4027829495.59|56279|
    |EMP0005|Maria Hernandez|3774396363.16|53276|
    |EMP0003|Daisy Torres|3701720195.87|52229|
    |EMP0006|David De Guzman|2745957381.67|38226|
    |EMP0009|Michelle Flores|2621092080.84|37176|

    >**Business Insight**
    >
    >Comparing revenue generated by Sales Representatives helps identify top performers, coaching opportunities, and recognition candidates.

    [Back to previous](/README.md#sales-representative-dashboard)

    #### Top Sales Representatives

    ![Top Sales Representatives](/images/postgre_screenshots/postgre_TopSalesRepresentatives.png)

    Result:

    |full_name|total_sales|sales_rank|
    |:--------|----------:|---------:|
    |Paolo De Guzman|8509819043.50|1|
    |Michael Bautista|8167771578.81|2|
    |Irene Domingo|4027829495.59|3|

    >**Business Insight**
    >
    >Ranking Sales Representatives highlights
    top performers while accounting for ties
    in total sales revenue.

    [Back to previous](/README.md#sales-representative-dashboard)

    #### Average Order Value By Sales Representative

    ![Average Order Value By Sales Representative](/images/postgre_screenshots/postgre_AverageOrderValueBySalesRepresentative.png)

    Result:

    |full_name| average_order_value|
    |:--------|-------------------:|
    |David De Guzman|	71834.81|
    |Paolo De Guzman|	71638.11|
    |Irene Domingo|	71568.96|
    |Michael Bautista|	71241.54|
    |Daisy Torres|	70874.81|
    |Maria Hernandez|	70846.09|
    |Michelle Flores|	70504.95|

    >**Business Insight**
    >
    >Representatives with high average order
    values may excel at upselling or handling
    higher-value customer accounts.

    [Back to previous](/README.md#sales-representative-dashboard)

    #### Cancelled Orders By Sales Representative

    ![Cancelled Orders By Sales Representative](/images/postgre_screenshots/postgre_CancelledOrdersBySalesRepresentative.png)

    >**Business Insight**
    >
    >A high number of cancelled orders may
    indicate customer dissatisfaction,
    order-entry errors, or operational issues
    that deserve further investigation.

    [Back to previous](/README.md#sales-representative-dashboard)

    #### Sales by Employment Type

    ![Sales by Employment Type](/images/postgre_screenshots/postgre_SalesByEmploymentType.png)

    >**Business Insight**
    >
    >Comparing employment types may help
    management evaluate workforce composition
    and overall sales contribution.

    [Back to previous](/README.md#sales-representative-dashboard)

    ### Supplier KPIs

    #### Top Suppliers by Sales Revenue

    ![Top Suppliers by Sales Revenue](/images/postgre_screenshots/postgre_TopSuppliersBySalesRevenue.png)

    Result:

    |supplier_id|supplier_name|total_sales|
    |:----------|:------------|----------:|
    |SUP0004|Golden Axis Business Solutions|	10725593151.15|
    |SUP0002|MetroTech Distribution Corporation|	7762257809.74|
    |SUP0015|Summit Industrial Supply|	7482931644.17|
    |SUP0014|Optimum Tech Traders|	1190222861.19|
    |SUP0013|ExcelPro Distribution|	825517982.58|
    |SUP0003|Vertex Industrial Traders|	796509769.50|
    |SUP0006|NorthPeak Technology Supply|	739333627.36|
    |SUP0007|Alliance Office Products|	736107892.38|
    |SUP0012|Horizon Business Solutions|	709388530.51|
    |SUP0001|PrimeSource Office Supplies Inc.|	648768839.02|
    |SUP0010|BluePeak Office Systems|	634696383.07|
    |SUP0016|CoreLink Office Products|	358291932.65|
    |SUP0008|Pinnacle Distribution Group|	356252731.51|
    |SUP0005|Pacific Office Essentials|	267886291.27|
    |SUP0009|EastBridge Business Supply|	184570868.78|
    |SUP0018|Unity Business Essentials|	72541704.00|
    |SUP0011|Sterling Office Supply|	57714120.56|

    >**Business Insight**
    >
    >Suppliers whose products generate strong
    sales are strategically important and may
    deserve stronger purchasing partnerships.

    [Back to previous](/README.md#suppliers-dashboard)

    #### Top Suppliers by Profit

    ![Top Suppliers by Profit](/images/postgre_screenshots/postgre_TopSuppliersByProfit.png)

    Result:

    |supplier_name|total_profit|
    |:------------|-----------:|
    |Golden Axis Business Solutions|	2157034558.95|
    |Summit Industrial Supply|	1519333201.87|
    |MetroTech Distribution Corporation|	1446940605.06|
    |Optimum Tech Traders|	251144426.96|
    |Vertex Industrial Traders|	196522672.06|
    |ExcelPro Distribution|	172463964.42|
    |PrimeSource Office Supplies Inc.|	166930967.86|
    |Alliance Office Products|	146852532.04|
    |BluePeak Office Systems|	142944066.06|
    |NorthPeak Technology Supply|	133672679.33|
    |Horizon Business Solutions|	125189716.97|
    |Pinnacle Distribution Group|	74002405.87|
    |CoreLink Office Products|	71380850.70|
    |Pacific Office Essentials|	67025826.56|
    |EastBridge Business Supply|	42081699.73|
    |Sterling Office Supply|	14767606.36|
    |Unity Business Essentials|	14034534.78|

    >**Business Insight**
    >
    >Profitability should be considered alongside
    sales volume when evaluating supplier
    performance and sourcing decisions.

    [Back to previous](/README.md#suppliers-dashboard)

    #### Product Portfolio by Supplier

    ![Product Portfolio by Supplier](/images/postgre_screenshots/postgre_ProductPortfolioBySupplier.png)

    Result:

    |supplier_name|total_products|
    |:------------|-------------:|
    |NorthPeak Technology Supply|	5|
    |Golden Axis Business Solutions|	5|
    |Summit Industrial Supply|	4|
    |Vertex Industrial Traders|	4|
    |MetroTech Distribution Corporation|	4|
    |Pacific Office Essentials|	4|
    |Optimum Tech Traders|	3|
    |CoreLink Office Products|	3|
    |Alliance Office Products|	3|
    |PrimeSource Office Supplies Inc.|	3|
    |Pinnacle Distribution Group|	2|
    |EastBridge Business Supply|	2|
    |BluePeak Office Systems|	2|
    |ExcelPro Distribution|	2|
    |Horizon Business Solutions|	2|
    |Unity Business Essentials|	1|
    |Sterling Office Supply|	1|

    >**Business Insight**
    >
    >Suppliers with broader product portfolios
    may simplify procurement by reducing the
    number of vendors required.

    [Back to previous](/README.md#suppliers-dashboard)

    #### Average Selling Price by Suppier

    ![Average Selling Price by Suppier](/images/postgre_screenshots/postgre_AverageSellingPriceBySupplier.png)

    Result:

    |supplier_name|average_selling_price|
    |:------------|--------------------:|
    |Summit Industrial Supply|	49502.20|
    |Golden Axis Business Solutions|	49489.78|
    |MetroTech Distribution Corporation|	45140.82|
    |ExcelPro Distribution|	11940.65|
    |BluePeak Office Systems|	10343.57|
    |PrimeSource Office Supplies Inc.|	9961.50|
    |Alliance Office Products|	7036.28|
    |Pinnacle Distribution Group|	5825.10|
    |Horizon Business Solutions|	5506.97|
    |Optimum Tech Traders|	5101.69|
    |Vertex Industrial Traders|	4609.12|
    |Unity Business Essentials|	3365.33|
    |NorthPeak Technology Supply|	2749.72|
    |Sterling Office Supply|	2651.03|
    |Pacific Office Essentials|	1341.62|
    |CoreLink Office Products|	1275.65|
    |EastBridge Business Supply|	985.23|

    >**Business Insight**
    >
    >Higher average selling prices may indicate
    premium product lines or specialized
    product offerings.

    [Back to previous](/README.md#suppliers-dashboard)

    #### Supplier Status Distribution

    ![Supplier Status Distribution](/images/postgre_screenshots/postgre_SupplierStatusDistribution.png)

    >**Business Insight**
    >
    >Monitoring supplier status helps ensure
    that purchasing activities rely primarily
    on active and approved suppliers.

    [Back to previous](/README.md#suppliers-dashboard)

    #### Average Lead Time by Supplier

    ![Average Lead Time by Supplier](/images/postgre_screenshots/postgre_AverageLeadTimeBySupplier.png)

    Result:

    |supplier_name|average_lead_time_days|
    |:------------|---------------------:|
    |BluePeak Office Systems|	27|
    |Vertex Industrial Traders|	26|
    |Alliance Office Products|	26|
    |MetroTech Distribution Corporation|	25|
    |Optimum Tech Traders|	24|
    |Pinnacle Distribution Group|	22|
    |Pacific Office Essentials|	20|
    |Horizon Business Solutions|	20|
    |NextWave Distribution|	18|
    |EastBridge Business Supply|	17|
    |Summit Industrial Supply|	16|
    |Unity Business Essentials|	12|
    |CoreLink Office Products|	7|
    |NorthPeak Technology Supply|	5|
    |PrimeSource Office Supplies Inc.|	5|
    |Sterling Office Supply|	5|
    |Golden Axis Business Solutions|	5|
    |ExcelPro Distribution|	3|

    >**Business Insight**
    >
    >Long supplier lead times may require higher
    safety stock levels and earlier purchasing
    decisions to reduce the risk of stockouts.

    [Back to previous](/README.md#suppliers-dashboard)

    ### Inventory KPIs

    #### Inventory Summary

    ![Inventory Summary](/images/postgre_screenshots/postgre_InventorySummary.png)

    >**Business Insight**
    >
    >This summary provides a high-level view
    of the company's inventory available for
    fulfilling customer demand.

    [Back to previous](/README.md#inventory-dashboard)

    #### Inventory Status Distribution

    ![Inventory Status Distribution](/images/postgre_screenshots/postgre_InventoryStatusDistribution.png)

    >**Business Insight**
    >
    >Monitoring inventory status helps identify
    how many products are adequately stocked,
    running low, or already out of stock.

    [Back to previous](/README.md#inventory-dashboard)

    #### Products Below Reorder Level

    ![Products Below Reorder Level](/images/postgre_screenshots/postgre_ProductsBelowReorderLevel_InventoryTable.png)

    >**Business Insight**
    >
    >Products below their reorder level should
    be prioritized for replenishment to reduce
    the likelihood of stock shortages.

    [Back to previous](/README.md#inventory-dashboard)

    #### Highest Inventory Levels

    ![Highest Inventory Levels](/images/postgre_screenshots/postgre_HighestInventoryLevels.png)

    >**Business Insight**
    >
    >Products with unusually high inventory
    may represent slow-moving stock or
    intentional inventory buffering.

    [Back to previous](/README.md#inventory-dashboard)

    #### Inventory by Product Category

    ![Inventory by Product Category](/images/postgre_screenshots/postgre_InventoryByProductCategory.png)

    >**Business Insight**
    >
    >Category-level inventory supports
    capacity planning and warehouse
    space allocation decisions.

    [Back to previous](/README.md#inventory-dashboard)

    #### Products Without Stock Movement

    ![Products Without Stock Movement](/images/postgre_screenshots/postgre_ProductsWithoutStockMovement.png)

    >**Business Insight**
    >
    >Products with no recorded stock movement
    may indicate new products, inactive items,
    or products with no recent customer demand.

    [Back to previous](/README.md#inventory-dashboard)

    #### Inventory Value

    ![Inventory Value](/images/postgre_screenshots/postgre_InventoryValue.png)

    >**Business Insight**
    >
    >Inventory value represents capital tied
    up in warehouse stock and is an important
    metric for inventory management.

    [Back to previous](/README.md#inventory-dashboard)

    ### Profitability KPIs

    #### Profitability Summary

    ![Profitability Summary](/images/postgre_screenshots/postgre_ProfitabilitySummary.png)

    >**Business Insight**
    >
    >This summary provides management with an
    overall view of business profitability and
    the percentage of revenue retained as profit.

    [Back to previous](/README.md#profitability-dashboard)

    #### Most Profitable Products

    ![Most Profitable Products](/images/postgre_screenshots/postgre_MostProfitableProducts.png)

    Result:

    |product_name|total_profit|
    |:-----------|-----------:|
    |NovaBook Ultra 18-inch|	848411908.71|
    |ApexStation Compact|	553763795.44|
    |ApexBook Pro 16-inch|	525389986.93|
    |NovaStation Workstation|	525076011.64|
    |ApexBook Pro 14-inch|	495962757.32|
    |ApexBook Essential 13-inch|	425587860.81|
    |NovaStation Tower|	367715312.35|
    |ApexStation Pro|	357554812.95|
    |NovaStation Mini|	352924626.57|
    |NovaBook Air 14-inch|	337277807.00|

    >**Business Insight**
    >
    >Products generating the highest profit
    should remain a strategic focus for
    inventory planning and sales efforts.

    [Back to previous](/README.md#profitability-dashboard)

    #### Profit Margin by Category

    ![Profit Margin by Category](/images/postgre_screenshots/postgre_ProfitMarginByCategory.png)

    Result:

    |category|total_sales|total_cost|total_profit|profit_margin_pct|
    |:-------|----------:|---------:|-----------:|----------------:|
    |Office Equipment|	779024663.58|	583291554.58|	195733109.00|	25.13|
    |Accessories|	810749092.70|	630260715.71|	180488376.99|	22.26|
    |Monitor|	990949114.58|	774002642.65|	216946471.93|	21.89|
    |Networking|	1505898300.01|	1184185910.98|	321712389.03|	21.36|
    |Printer|	1561625874.96|	1242309378.50|	319316496.46|	20.45|
    |Desktop|	10725593151.15|	8568558592.20|	2157034558.95|	20.11|
    |Storage|	1929556488.55|	1544739382.26|	384817106.29|	19.94|
    |Laptop|	15245189453.91|	12278915646.98|	2966273806.93|	19.46|

    >**Business Insight**
    >
    >Profit margin highlights which categories
    retain the largest proportion of revenue
    after covering product costs.

    [Back to previous](/README.md#profitability-dashboard)

    #### Average Profit per Order

    ![Average Profit per Order](/images/postgre_screenshots/postgre_AverageProfitPerOrder.png)

    >**Business Insight**
    >
    >Average profit per order provides a useful
    benchmark for evaluating pricing strategies
    and sales performance over time.

    [Back to previous](/README.md#profitability-dashboard)

    #### Profit by Order Source

    ![Profit by Order Source](/images/postgre_screenshots/postgre_ProfitByOrderSource.png)

    Result:

    |order_source|total_profit|profit_margin_pct|
    |:-----------|-----------:|----------------:|
    |Sales Representative|	4861674714.46|	20.10|
    |Phone|	807540601.48|	20.13|
    |Email|	664719218.25|	20.02|
    |Walk-in|	269991481.89|	20.11|
    |Website|	138396299.50|	20.02|

    >**Business Insight**
    >
    >Comparing profitability across sales channels
    helps identify where revenue translates into
    the strongest financial returns.

    [Back to previous](/README.md#profitability-dashboard)

    #### Highest Product Profit Margin

    ![Highest Product Profit Margin](/images/postgre_screenshots/postgre_HighestProductProfitMargin.png)

    Result:

    |product_name|average_profit_margin_pct|
    |:-----------|------------------------:|
    |SwiftLink Router AX1800|	28.04|
    |FlexMouse Wired|	27.74|
    |SwiftLink Router AC1200|	27.10|
    |CorePrint Label Standard|	26.79|
    |FlexHub 4-Port|	26.30|
    |FlexWebcam HD|	26.19|
    |OfficePro Document Scanner ADF|	26.16|
    |OfficePro Laminator A4|	25.25|
    |OfficePro Projector Business|	25.18|
    |OfficePro Shredder Personal|	24.69|

    >**Business Insight**
    >
    >High-margin products may deserve increased
    marketing attention because they generate
    more profit for each peso of sales revenue.

    [Back to previous](/README.md#profitability-dashboard)

    ### Views

    #### View for Sales Summary

    ![View for Sales Summary](/images/postgre_screenshots/postgre_vw_sales_summary.png)

    [Back to previous](/README.md#views)

    #### View for Product Performance

    ![View for Product Performance](/images/postgre_screenshots/postgre_vw_product_performance.png)

    [Back to previous](/README.md#views)

    #### View for Customer Performance

    ![View for Customer Performance](/images/postgre_screenshots/postgre_vw_customer_performance.png)

    [Back to previous](/README.md#views)

    #### View for Inventory Status

    ![View for Inventory Status](/images/postgre_screenshots/postgre_vw_inventory_status.png)

    [Back to previous](/README.md#views)

    #### View for Supplier Performance

    ![View for Supplier Performance](/images/postgre_screenshots/postgre_vw_supplier_performance.png)

    [Back to previous](/README.md#views)

    ### Verify Reporting Views

    #### vw_sales_summary

    ![vw_sales_summary](/images/postgre_screenshots/postgre_verify_vw_sales_summary.png)

    [Back to previous](/README.md#verify-reporting-views)

    #### vw_product_performance

    ![vw_product_performance](/images/postgre_screenshots/postgre_verify_vw_product_performance.png)

    [Back to previous](/README.md#verify-reporting-views)

    #### vw_customer_performance

    ![vw_customer_performance](/images/postgre_screenshots/postgre_verify_vw_customer_performance.png)

    [Back to previous](/README.md#verify-reporting-views)

    #### vw_inventory_status

    ![vw_inventory_status](/images/postgre_screenshots/postgre_verify_vw_inventory_status.png)

    [Back to previous](/README.md#verify-reporting-views)

    #### vw_supplier_performance

    ![vw_supplier_performance](/images/postgre_screenshots/postgre_verify_vw_supplier_performance.png)

    [Back to previous](/README.md#verify-reporting-views)

Following this sequence ensures that all table relationships are established before data is imported and analyzed.

---

## Database Design

The SQL implementation follows the database design documented in:

```text
docs/DATABASE_SCHEMA.md
```

The schema uses a normalized relational structure with primary keys and foreign keys to maintain data integrity while supporting warehouse operations, inventory management, customer management, supplier management, and sales reporting.

---

## Dataset Source

Only the validated datasets stored in:

```text
data/cleaned/
```

are imported into PostgreSQL. [click here to see the cleaned data:](/data/cleaned/)

The intentionally modified datasets stored in:

```text
data/messy/
```

exist solely for demonstrating data cleaning in Power Query and are **not** imported into the database. [click here to see the messy data:](/data//messy/)

---

## Project Workflow

```text
Python Dataset Generation
            │
            ▼
Validated CSV Files (data/cleaned)
            │
            ▼
PostgreSQL Database
            │
            ▼
Data Validation
            │
            ▼
SQL Business Analysis
            │
            ▼
Excel Reporting
            │
            ▼
Power BI Dashboard
```
