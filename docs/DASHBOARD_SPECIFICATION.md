# Dashboard Specification

## Overview

The LOTS Corp. Warehouse Analytics Power BI report is organized into seven analytical dashboard pages. Each page focuses on a specific business area while using common Year and Month filtering where applicable.

The specifications below are based on the final Power BI report  for this project. The screenshots are documented separately in [Power BI Documentation](/powerbi/README.md).

---

# 1. Executive Dashboard

## Purpose

Provides a high-level overview of sales, profitability, order volume, product performance, and order-source performance for executive-level monitoring.

## Filters
- Year
- Month
- Product Category
- Order Source

## KPI Cards
- Total Sales
- Total Profit
- Profit Margin %
- Total Orders
- Average Order Value
- Out-of-Stock Products

## Visualizations

### Monthly Sales Trend
- Type: Line chart
- Measure: Total Sales
- Dimension: Year-Month

### Sales by Category
- Type: Horizontal bar chart
- Measure: Total Sales
- Dimension: Product Category

### Order Status Distribution
- Type: Donut chart
- Measure: Order count
- Dimension: Order Status
- Statuses shown: Delivered, Cancelled, Returned, Shipped, Processing

### Sales by Order Source
- Type: Column chart
- Measure: Total Sales
- Dimension: Order Source

---

# 2. Customer Analysis

## Purpose

Analyzes customer composition and sales performance across customer types, geographic regions, industries, and individual customers.

## Filters
- Year
- Month
- Customer Type
- Industry
- Province

## KPI Cards
- Total Customers
- Total Sales
- Average Order Value
- Average Customer Sales

## Visualizations

### Sales by Customer Type
- Type: Donut chart
- Measure: Total Sales
- Dimension: Customer Type

### Sales by Region
- Type: Column chart
- Measure: Total Sales
- Dimension: Region

### Top 10 Customers by Sales
- Type: Horizontal bar chart
- Measure: Total Sales
- Dimension: Customer
- Filter: Top 10

### Sales by Industry
- Type: Horizontal bar chart
- Measure: Total Sales
- Dimension: Industry

---

# 3. Employee Performance

## Purpose

Evaluates sales representative performance using sales, profit, order volume, and average order value.

## Filters
- Year
- Month
- Employee Name
- Position

## KPI Cards
- Total Sales Representatives
- Total Sales
- Total Profit
- Average Order Value

## Visualizations

### Sales by Representative
- Type: Horizontal bar chart
- Measure: Total Sales
- Dimension: Employee / Sales Representative

### Orders Handled
- Type: Column chart
- Measure: Orders Handled
- Dimension: Employee / Sales Representative

### Profit by Representative
- Type: Horizontal bar chart
- Measure: Total Profit
- Dimension: Employee / Sales Representative

### Average Order Value by Representative
- Type: Horizontal bar chart
- Measure: Average Order Value
- Dimension: Employee / Sales Representative

---

# 4. Products & Inventory Analysis

## Purpose

Monitors product activity, inventory availability, product sales and profit performance, category stock levels, and products with the lowest available stock.

## Filters
- Year
- Month
- Product Category
- Supplier Name

## KPI Cards
- Active Products
- Total Quantity Sold
- Out-of-Stock Products
- Average Current Stock

## Visualizations

### Inventory Status Distribution
- Type: Donut chart
- Measure: Inventory record count
- Dimension: Inventory Status

### Top 10 Products by Sales
- Type: Horizontal bar chart
- Measure: Total Sales
- Dimension: Product
- Filter: Top 10

### Top 10 Products by Profit
- Type: Horizontal bar chart
- Measure: Total Profit
- Dimension: Product
- Filter: Top 10

### Current Stock by Category
- Type: Column chart
- Measure: Current Stock
- Dimension: Product Category

### Lowest Available Stock
- Type: Horizontal bar chart
- Measure: Available Stock
- Dimension: Product

---

# 5. Profitability Analysis

## Purpose

Analyzes overall profitability and evaluates profit trends, product profitability, category profitability, and supplier contribution.

## Filters
- Year
- Month
- Product Category
- Supplier Name

## KPI Cards
- Total Profit
- Total Sales
- Profit Margin %
- Average Profit per Order

## Visualizations

### Monthly Profit Trend
- Type: Line chart
- Measure: Total Profit
- Dimension: Year-Month

### Top 10 Products by Profit
- Type: Horizontal bar chart
- Measure: Total Profit
- Dimension: Product
- Filter: Top 10

### Profit by Category
- Type: Horizontal bar chart
- Measure: Total Profit
- Dimension: Product Category

### Profit by Supplier
- Type: Horizontal bar chart
- Measure: Total Profit
- Dimension: Supplier

---

# 6. Sales Analysis

## Purpose

Provides detailed analysis of sales performance, sales volume, selling price, discount impact, product categories, customer types, and order sources.

## Filters
- Year
- Month
- Product Category
- Order Source

## KPI Cards
- Total Sales
- Total Quantity Sold
- Average Selling Price
- Total Discount Amount

## Visualizations

### Sales by Product Category
- Type: Horizontal bar chart
- Measure: Total Sales
- Dimension: Product Category

### Monthly Sales Trend
- Type: Line chart
- Measure: Total Sales
- Dimension: Year-Month

### Top 10 Products by Sales
- Type: Horizontal bar chart
- Measure: Total Sales
- Dimension: Product
- Filter: Top 10

### Sales by Customer Type
- Type: Donut chart
- Measure: Total Sales
- Dimension: Customer Type

### Sales by Order Source
- Type: Column chart
- Measure: Total Sales
- Dimension: Order Source

---

# 7. Supplier Analysis

## Purpose

Evaluates supplier contribution to sales and profit while providing visibility into supplier product coverage and lead-time performance.

## Filters
- Year
- Month
- Product Category
- Supplier Name

## KPI Cards
- Total Suppliers
- Total Sales
- Total Profit
- Average Supplier Lead Time

## Visualizations

### Products per Supplier
- Type: Column chart
- Measure: Products per Supplier
- Dimension: Supplier

### Sales by Supplier
- Type: Horizontal bar chart
- Measure: Total Sales
- Dimension: Supplier

### Profit by Supplier
- Type: Horizontal bar chart
- Measure: Total Profit
- Dimension: Supplier

### Supplier Lead Time
- Type: Horizontal bar chart
- Measure: Average Supplier Lead Time
- Dimension: Supplier

---

# 8. Shared Measures

The report uses a centralized **Measure Table** to organize DAX measures by analytical area.

## Customer Analysis
- `Average Customer Sales`

## Employee Performance
- `Orders Handled`
- `Total Sales Representatives`

## Executive KPIs
- `Active Products`
- `Average Order Value`
- `Out-of-Stock Products`
- `Profit Margin %`
- `Total Cost`
- `Total Customers`
- `Total Orders`
- `Total Products`
- `Total Profit`
- `Total Quantity Sold`
- `Total Sales`

## Products & Inventory Analysis
- `Available Stock`
- `Average Current Stock`
- `Current Stock`
- `Inventory Records`
- `Reserved Stock`

## Profitability Analysis
- `Average Profit per Order`
- `Total Sales Orders`

## Sales Analysis
- `Average Discount %`
- `Average Selling Price`
- `Total Discount Amount`

## Supplier Analysis
- `Average Supplier Lead Time`
- `Products per Supplier`
- `Total Suppliers`

---

# 9. Date Dimension

The report contains a dedicated `Dim Date` table for time-based analysis.

## Fields
- Date
- Day
- Day Name
- Month
- Month Number
- Month Short
- Quarter
- Year
- Year Month

The date dimension supports the Year, Month, and Year-Month analysis used throughout the report.

---

# 10. Data Model Tables

The Power BI model contains the following source tables:

- `public customers`
- `public employees`
- `public inventory`
- `public order_details`
- `public orders`
- `public products`
- `public suppliers`

A dedicated **Measure Table** is used to organize DAX measures, and `Dim Date` provides the calendar attributes used for time-based reporting.

---

# 11. Dashboard Design Notes

The dashboard pages use distinct visual themes to separate analytical areas:

- Executive Dashboard: Blue
- Customer Analysis: Green
- Employee Performance: Cyan/teal
- Products & Inventory Analysis: Yellow/lime
- Profitability Analysis: Green
- Sales Analysis: Green/teal
- Supplier Analysis: Orange

The report uses slicers at the top of each page to allow users to interactively filter the displayed KPIs and visualizations.
