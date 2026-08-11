/*
============================================================
LOTS Corp. Warehouse Analytics Portfolio

SQL Analysis Queries

This script contains analytical SQL queries developed for the
LOTS Corp. Warehouse Analytics Portfolio. The analyses cover
executive KPIs, sales, customers, products, employees,
suppliers, inventory, and profitability.

The queries are intended to demonstrate SQL skills for
business reporting and decision-making using a normalized
PostgreSQL database.
============================================================
*/

-- ============================================================
-- KPI 1
-- Total Sales Revenue
--
-- Business Question:
-- How much revenue has LOTS Corp. generated from completed sales?
--
-- Notes:
-- Excludes cancelled orders.
-- Revenue is calculated from order_details.line_total.
-- ============================================================
SELECT current_database();

SELECT

    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales_revenue

FROM orders o

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled';

-- ============================================================
-- KPI 2
-- Total Profit
--
-- Business Question:
-- How much profit has LOTS Corp. earned
-- from completed sales?
-- ============================================================

SELECT

    ROUND(
        SUM(od.line_profit),
        2
    ) AS total_profit

FROM orders o

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled';

-- ============================================================
-- KPI 3
-- Total Orders
--
-- Business Question:
-- How many sales orders have been created?
--
-- Note:
-- includes cancel orders
-- ============================================================

SELECT

    COUNT(*) AS total_orders

FROM orders;

-- ============================================================
-- KPI 4
-- Total Cancelled Orders
--
-- Business Question:
-- How many customer orders were cancelled?
-- ============================================================

SELECT

    COUNT(*) AS cancelled_orders

FROM orders

WHERE order_status = 'Cancelled';

-- ============================================================
-- KPI 5
-- Total Returned Orders
--
-- Business Question:
-- How many customer orders were returned?
-- ============================================================

SELECT

    COUNT(*) AS returned_orders

FROM orders

WHERE order_status = 'Returned';

-- ============================================================
-- KPI 6
-- Average Order Value (AOV)
--
-- Business Question:
-- What is the average revenue generated
-- per completed customer order?
-- ============================================================

SELECT

    ROUND(

        SUM(od.line_total)

        /

        COUNT(DISTINCT o.order_id),

        2

    ) AS average_order_value

FROM orders o

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled';

-- ============================================================
-- Sales Analysis 1
-- Annual Sales Revenue
--
-- Business Question:
-- How much sales revenue was generated each year?
-- ============================================================

SELECT

    EXTRACT(YEAR FROM o.order_date) AS order_year,

    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales

FROM orders o

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    EXTRACT(YEAR FROM o.order_date)

ORDER BY
    order_year;

-- ============================================================
-- Sales Analysis 2
-- Monthly Sales Trend
--
-- Business Question:
-- How has monthly sales revenue changed over time?
-- ============================================================

SELECT

    DATE_TRUNC(
        'month',
        o.order_date
    ) AS sales_month,

    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales

FROM orders o

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY

    DATE_TRUNC(
        'month',
        o.order_date
    )

ORDER BY

    sales_month;

-- ============================================================
-- Sales Analysis 3
-- Sales by Order Source
--
-- Business Question:
-- Which sales channels generate
-- the highest revenue?
-- ============================================================

SELECT
    o.order_source,
    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales,

    COUNT(DISTINCT o.order_id) AS total_orders

FROM orders o

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    o.order_source
ORDER BY
    total_sales DESC

-- ============================================================
-- Sales Analysis 4
-- Orders by Status
--
-- Business Question:
-- How are customer orders distributed
-- across different statuses?
-- ============================================================

SELECT

    order_status,

    COUNT(*) AS total_orders

FROM orders

GROUP BY

    order_status

ORDER BY

    total_orders DESC;

-- ============================================================
-- Sales Analysis 5
-- Payment Status Distribution
--
-- Business Question:
-- What is the distribution of payment statuses?
-- ============================================================

SELECT

    payment_status,

    COUNT(*) AS total_orders

FROM orders

GROUP BY

    payment_status

ORDER BY

    total_orders DESC;

-- ============================================================
-- Sales Analysis 6
-- Average Order Value by Order Source
--
-- Business Question:
-- Which sales channel produces
-- the highest average order value?
-- ============================================================

SELECT
    o.order_source,

    ROUND(
        SUM(od.line_total)
        /
        COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value

FROM orders o

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    o.order_source
ORDER BY
    average_order_value DESC;

-- ============================================================
-- Customer Analysis 1
-- Top 10 Customers by Sales Revenue
--
-- Business Question:
-- Which customers generate the highest revenue?
-- ============================================================

SELECT
    c.customer_id,
    c.customer_name,
    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY
    total_sales DESC
LIMIT 10;

/*
Business Insight:

A small group of customers often contributes
a significant share of total revenue.

These customers may be candidates for
priority account management, loyalty programs,
or targeted retention strategies.
*/

-- ============================================================
-- Customer Analysis 2
-- Sales by Customer Type
--
-- Business Question:
-- Which customer type generates
-- the highest sales revenue?
-- ============================================================

SELECT
    c.customer_type,
    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales,
    COUNT(DISTINCT c.customer_id)
        AS total_customers

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    c.customer_type
ORDER BY
    total_sales DESC;
	
/*
Business Insight:

Comparing revenue across customer types
helps identify the organization's primary
market segment and supports sales strategy.
*/

-- ============================================================
-- Customer Analysis 3
-- Sales by Industry
--
-- Business Question:
-- Which industries generate
-- the highest sales revenue?
-- ============================================================

SELECT
    c.industry,
    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales
FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    c.industry
ORDER BY
    total_sales DESC;

/*
Business Insight:

High-performing industries represent
important market opportunities and may
justify additional marketing or sales efforts.
*/

-- ============================================================
-- Customer Analysis 4
-- Customer Status Distribution
--
-- Business Question:
-- How many customers are currently
-- Active or Inactive?
-- ============================================================

SELECT
    status,
    COUNT(*) AS total_customers

FROM customers

GROUP BY
    status
ORDER BY
    total_customers DESC;

/*
Business Insight:

A growing number of inactive customers
may indicate customer churn and could
signal the need for retention initiatives.
*/

-- ============================================================
-- Customer Analysis 5
-- Average Revenue per Customer
--
-- Business Question:
-- On average, how much revenue
-- does each purchasing customer generate?
-- ============================================================

SELECT
    ROUND(
        SUM(od.line_total)
        /
        COUNT(DISTINCT c.customer_id),
        2
    ) AS average_customer_revenue

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN order_details od
ON o.order_id = od.order_id

WHERE o.order_status <> 'Cancelled';

/*
Business Insight:

Average customer revenue provides
a baseline for evaluating customer value
and measuring improvements over time.
*/

-- ============================================================
-- Customer Analysis 6
-- Top Customers by Number of Orders
--
-- Business Question:
-- Which customers place
-- the most orders?
-- ============================================================

SELECT
    c.customer_name,
    COUNT(DISTINCT o.order_id)
        AS total_orders
FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

GROUP BY
    c.customer_name
ORDER BY
    total_orders DESC
LIMIT 10;

/*
Business Insight:

Customers with frequent purchases may
represent long-term relationships even if
their individual order values are modest.
*/

-- ============================================================
-- Product Analysis 1
-- Top 10 Products by Sales Revenue
--
-- Business Question:
-- Which products generate the highest sales revenue?
-- ============================================================

SELECT
    p.product_id,
    p.product_name,
    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales

FROM products p

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    p.product_id,
    p.product_name
ORDER BY
    total_sales DESC
LIMIT 10;

/*
Business Insight:

High-revenue products represent the company's
best-performing offerings and should receive
continued inventory availability and marketing support.
*/

-- ============================================================
-- Product Analysis 2
-- Top 10 Products by Profit
--
-- Business Question:
-- Which products generate the highest profit?
-- ============================================================

SELECT
    p.product_name,
    ROUND(
        SUM(od.line_profit),
        2
    ) AS total_profit

FROM products p

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    p.product_name
ORDER BY
    total_profit DESC
LIMIT 10;

/*
Business Insight:

Products with high profitability contribute
most to overall business growth and may deserve
greater sales focus.
*/

-- ============================================================
-- Product Analysis 3
-- Top Selling Products
--
-- Business Question:
-- Which products sell the greatest number of units?
-- ============================================================

SELECT
    p.product_name,
    SUM(od.quantity)
        AS units_sold

FROM products p

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    p.product_name
ORDER BY
    units_sold DESC
LIMIT 10;

/*
Business Insight:

Products with consistently high sales volume
require careful inventory planning to reduce
the risk of stock shortages.
*/

-- ============================================================
-- Product Analysis 4
-- Sales by Product Category
--
-- Business Question:
-- Which product categories generate
-- the highest sales revenue?
-- ============================================================

SELECT
    p.category,
    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales

FROM products p

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    p.category
ORDER BY
    total_sales DESC;

/*
Business Insight:

Category-level analysis helps management
identify product segments that drive
overall company performance.
*/

-- ============================================================
-- Product Analysis 5
-- Profit by Product Category
--
-- Business Question:
-- Which product categories generate
-- the highest profit?
-- ============================================================

SELECT
    p.category,
    ROUND(
        SUM(od.line_profit),
        2
    ) AS total_profit

FROM products p

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE o.order_status <> 'Cancelled'

GROUP BY
    p.category
ORDER BY
    total_profit DESC;
	
/*
Business Insight:

High-profit categories may justify
additional investment, promotions,
or product expansion.
*/

-- ============================================================
-- Product Analysis 6
-- Average Discount by Product
--
-- Business Question:
-- Which products receive
-- the highest average discount?
-- ============================================================

SELECT
    p.product_name,
    ROUND(
        AVG(
            od.discount_pct
        ) * 100,
        2
    ) AS average_discount_pct

FROM products p

JOIN order_details od
ON p.product_id = od.product_id

GROUP BY
    p.product_name
ORDER BY
    average_discount_pct DESC;

/*
Business Insight:

Products with consistently high discounts
may indicate aggressive pricing strategies
or lower customer demand.
*/

-- ============================================================
-- Product Analysis 7
-- Products Below Reorder Level
--
-- Business Question:
-- Which products require replenishment?
-- ============================================================

SELECT
    p.product_name,
    i.available_stock,
    p.reorder_level,
    i.inventory_status

FROM products p

JOIN inventory i
ON p.product_id = i.product_id

WHERE
    i.available_stock
    <=
    p.reorder_level
ORDER BY
    i.available_stock ASC;

/*
Business Insight:

Products below their reorder level should
be reviewed for replenishment to minimize
the risk of stockouts.
*/

-- ============================================================
-- Employee Analysis 1
-- Sales Revenue by Sales Representative
--
-- Business Question:
-- Which Sales Representatives generate
-- the highest sales revenue?
-- ============================================================

SELECT
    e.employee_id,
    e.full_name,
    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales,

    COUNT(DISTINCT o.order_id)
        AS total_orders

FROM employees e

JOIN orders o
ON e.employee_id = o.sales_rep_id

JOIN order_details od
ON o.order_id = od.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    e.employee_id,
    e.full_name
ORDER BY
    total_sales DESC;

/*
Business Insight:

Comparing revenue generated by Sales
Representatives helps identify top performers,
coaching opportunities, and recognition candidates.
*/

-- ============================================================
-- Employee Analysis 2
-- Top Sales Representatives
--
-- Business Question:
-- Who are the highest-performing
-- Sales Representatives?
-- ============================================================
SELECT *

FROM (
    SELECT
        e.full_name,
        ROUND(
            SUM(od.line_total),
            2
        ) AS total_sales,
        RANK() OVER (
            ORDER BY
                SUM(od.line_total) DESC
        ) AS sales_rank

    FROM employees e

    JOIN orders o

    ON e.employee_id = o.sales_rep_id

    JOIN order_details od

    ON o.order_id = od.order_id

    WHERE
        o.order_status <> 'Cancelled'
    GROUP BY
        e.full_name
) ranked_sales
WHERE
    sales_rank <= 3
ORDER BY
    sales_rank;

/*
Business Insight:

Ranking Sales Representatives highlights
top performers while accounting for ties
in total sales revenue.
*/

-- ============================================================
-- Employee Analysis 3
-- Average Order Value by Sales Representative
--
-- Business Question:
-- Which Sales Representatives generate
-- the highest average order value?
-- ============================================================

SELECT
    e.full_name,
    ROUND(
        SUM(od.line_total)
        /
        COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value

FROM employees e

JOIN orders o
ON e.employee_id = o.sales_rep_id

JOIN order_details od
ON o.order_id = od.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    e.full_name
ORDER BY
    average_order_value DESC;

/*
Business Insight:

Representatives with high average order
values may excel at upselling or handling
higher-value customer accounts.
*/

-- ============================================================
-- Employee Analysis 4
-- Cancelled Orders by Sales Representative
--
-- Business Question:
-- Which Sales Representatives
-- handle the most cancelled orders?
-- ============================================================

SELECT
    e.full_name,
    COUNT(*) AS cancelled_orders
	
FROM employees e

JOIN orders o
ON e.employee_id = o.sales_rep_id

WHERE
    o.order_status = 'Cancelled'
GROUP BY
    e.full_name
ORDER BY
    cancelled_orders DESC;

/*
Business Insight:

A high number of cancelled orders may
indicate customer dissatisfaction,
order-entry errors, or operational issues
that deserve further investigation.
*/

-- ============================================================
-- Employee Analysis 5
-- Sales by Employment Type
--
-- Business Question:
-- How does sales performance vary
-- by employment type?
-- ============================================================

SELECT
    e.employment_type,
    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales,
    COUNT(DISTINCT o.order_id)
        AS total_orders

FROM employees e

JOIN orders o
ON e.employee_id = o.sales_rep_id

JOIN order_details od
ON o.order_id = od.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    e.employment_type
ORDER BY
    total_sales DESC;

/*
Business Insight:

Comparing employment types may help
management evaluate workforce composition
and overall sales contribution.
*/

-- ============================================================
-- Supplier Analysis 1
-- Top Suppliers by Sales Revenue
--
-- Business Question:
-- Which suppliers provide the products
-- that generate the highest sales revenue?
-- ============================================================

SELECT
    s.supplier_id,
    s.supplier_name,
    ROUND(
        SUM(od.line_total),
        2
    ) AS total_sales

FROM suppliers s

JOIN products p
ON s.supplier_id = p.supplier_id

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    s.supplier_id,
    s.supplier_name
ORDER BY
    total_sales DESC;

/*
Business Insight:

Suppliers whose products generate strong
sales are strategically important and may
deserve stronger purchasing partnerships.
*/

-- ============================================================
-- Supplier Analysis 2
-- Top Suppliers by Profit
--
-- Business Question:
-- Which suppliers contribute the highest
-- overall profit?
-- ============================================================

SELECT
    s.supplier_name,
    ROUND(
        SUM(od.line_profit),
        2
    ) AS total_profit

FROM suppliers s

JOIN products p
ON s.supplier_id = p.supplier_id

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    s.supplier_name
ORDER BY
    total_profit DESC;

/*
Business Insight:

Profitability should be considered alongside
sales volume when evaluating supplier
performance and sourcing decisions.
*/

-- ============================================================
-- Supplier Analysis 3
-- Product Portfolio by Supplier
--
-- Business Question:
-- Which suppliers provide the largest
-- number of products?
-- ============================================================

SELECT
    s.supplier_name,
    COUNT(p.product_id)
        AS total_products

FROM suppliers s

JOIN products p
ON s.supplier_id = p.supplier_id

GROUP BY
    s.supplier_name
ORDER BY
    total_products DESC;

/*
Business Insight:

Suppliers with broader product portfolios
may simplify procurement by reducing the
number of vendors required.
*/

-- ============================================================
-- Supplier Analysis 4
-- Average Selling Price by Supplier
--
-- Business Question:
-- Which suppliers provide the
-- highest-value products?
-- ============================================================

SELECT
    s.supplier_name,
    ROUND(
        AVG(p.selling_price),
        2
    ) AS average_selling_price

FROM suppliers s

JOIN products p
ON s.supplier_id = p.supplier_id

GROUP BY
    s.supplier_name
ORDER BY
    average_selling_price DESC;

/*
Business Insight:

Higher average selling prices may indicate
premium product lines or specialized
product offerings.
*/

-- ============================================================
-- Supplier Analysis 5
-- Supplier Status Distribution
--
-- Business Question:
-- How many suppliers are Active
-- versus Inactive?
-- ============================================================

SELECT
    supplier_status,
    COUNT(*) AS total_suppliers

FROM suppliers

GROUP BY
    supplier_status
ORDER BY
    total_suppliers DESC;

/*
Business Insight:

Monitoring supplier status helps ensure
that purchasing activities rely primarily
on active and approved suppliers.
*/

-- ============================================================
-- Supplier Analysis 6
-- Average Lead Time by Supplier
--
-- Business Question:
-- Which suppliers have the shortest
-- and longest average lead times?
-- ============================================================

SELECT
    s.supplier_name,
    ROUND(
        AVG(s.lead_time_days),
        0
    ) AS average_lead_time_days
FROM suppliers s

GROUP BY
    s.supplier_name
ORDER BY
    average_lead_time_days DESC;

/*
Business Insight:

Long supplier lead times may require higher
safety stock levels and earlier purchasing
decisions to reduce the risk of stockouts.
*/

-- ============================================================
-- Inventory Analysis 1
-- Inventory Summary
--
-- Business Question:
-- What is the overall inventory position
-- across all products?
-- ============================================================

SELECT

    SUM(current_stock) AS total_current_stock,

    SUM(reserved_stock) AS total_reserved_stock,

    SUM(available_stock) AS total_available_stock

FROM inventory;

/*
Business Insight:

This summary provides a high-level view
of the company's inventory available for
fulfilling customer demand.
*/

-- ============================================================
-- Inventory Analysis 2
-- Inventory Status Distribution
--
-- Business Question:
-- How are products distributed across
-- inventory statuses?
-- ============================================================

SELECT
    inventory_status,
    COUNT(*) AS total_products

FROM inventory

GROUP BY
    inventory_status
ORDER BY
    total_products DESC;

/*
Business Insight:

Monitoring inventory status helps identify
how many products are adequately stocked,
running low, or already out of stock.
*/

-- ============================================================
-- Inventory Analysis 3
-- Products Below Reorder Level
--
-- Business Question:
-- Which products require replenishment?
-- ============================================================

WITH inventory_monitor AS (
    SELECT
        p.product_name,
        p.reorder_level,
        i.available_stock,
        i.inventory_status

    FROM products p

    JOIN inventory i
    ON p.product_id = i.product_id
)

SELECT *
FROM inventory_monitor

WHERE
    available_stock <= reorder_level
ORDER BY
    available_stock ASC;

/*
Business Insight:

Products below their reorder level should
be prioritized for replenishment to reduce
the likelihood of stock shortages.
*/

-- ============================================================
-- Inventory Analysis 4
-- Highest Inventory Levels
--
-- Business Question:
-- Which products currently have
-- the largest inventory levels?
-- ============================================================

SELECT
    p.product_name,
    i.current_stock

FROM products p

JOIN inventory i
ON p.product_id = i.product_id

ORDER BY
    i.current_stock DESC
LIMIT 10;

/*
Business Insight:

Products with unusually high inventory
may represent slow-moving stock or
intentional inventory buffering.
*/

-- ============================================================
-- Inventory Analysis 5
-- Inventory by Product Category
--
-- Business Question:
-- Which product categories hold
-- the largest inventory quantities?
-- ============================================================

SELECT
    p.category,
    SUM(i.current_stock)
        AS total_stock

FROM products p

JOIN inventory i
ON p.product_id = i.product_id

GROUP BY
    p.category
ORDER BY
    total_stock DESC;

/*
Business Insight:

Category-level inventory supports
capacity planning and warehouse
space allocation decisions.
*/

-- ============================================================
-- Inventory Analysis 6
-- Products Without Stock Movement
--
-- Business Question:
-- Which products have never recorded
-- a stock movement?
-- ============================================================

SELECT
    p.product_name,
    i.inventory_status

FROM products p

JOIN inventory i
ON p.product_id = i.product_id

WHERE
    i.last_stock_movement IS NULL
ORDER BY
    p.product_name;

/*
Business Insight:

Products with no recorded stock movement
may indicate new products, inactive items,
or products with no recent customer demand.
*/

-- ============================================================
-- Inventory Analysis 7
-- Inventory Value
--
-- Business Question:
-- What is the estimated inventory value
-- based on current stock levels?
-- ============================================================

SELECT
    ROUND(
        SUM(
            i.current_stock
            * p.cost_price
        ),
        2
    ) AS inventory_value

FROM inventory i

JOIN products p
ON i.product_id = p.product_id;

/*
Business Insight:

Inventory value represents capital tied
up in warehouse stock and is an important
metric for inventory management.
*/

-- ============================================================
-- Profitability Analysis 1
-- Profitability Summary
--
-- Business Question:
-- What are the company's overall sales,
-- cost, profit, and profit margin?
-- ============================================================

WITH profitability_summary AS (

    SELECT
        SUM(line_total) AS total_sales,
        SUM(line_cost) AS total_cost,
        SUM(line_profit) AS total_profit

    FROM order_details od

    JOIN orders o
    ON od.order_id = o.order_id

    WHERE
        o.order_status <> 'Cancelled'
)

SELECT
    ROUND(total_sales, 2) AS total_sales,
    ROUND(total_cost, 2) AS total_cost,
    ROUND(total_profit, 2) AS total_profit,
    ROUND(
        (total_profit / total_sales) * 100,
        2
    ) AS profit_margin_pct

FROM profitability_summary;

/*
Business Insight:

This summary provides management with an
overall view of business profitability and
the percentage of revenue retained as profit.
*/

-- ============================================================
-- Profitability Analysis 2
-- Most Profitable Products
--
-- Business Question:
-- Which products generate the
-- highest overall profit?
-- ============================================================

SELECT
    p.product_name,
    ROUND(
        SUM(od.line_profit),
        2
    ) AS total_profit

FROM products p

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    p.product_name
ORDER BY
    total_profit DESC
LIMIT 10;

/*
Business Insight:

Products generating the highest profit
should remain a strategic focus for
inventory planning and sales efforts.
*/

-- ============================================================
-- Profitability Analysis 3
-- Profit Margin by Category
--
-- Business Question:
-- Which product categories achieve
-- the highest profit margins?
-- ============================================================
WITH category_profitability AS (
    SELECT
        p.category,
        SUM(od.line_total) AS total_sales,
        SUM(od.line_cost) AS total_cost,
        SUM(od.line_profit) AS total_profit

    FROM products p

    JOIN order_details od
    ON p.product_id = od.product_id

    JOIN orders o
    ON od.order_id = o.order_id

    WHERE
        o.order_status <> 'Cancelled'
    GROUP BY
        p.category
)
SELECT
    category,
    ROUND(total_sales, 2) AS total_sales,
    ROUND(total_cost, 2) AS total_cost,
    ROUND(total_profit, 2) AS total_profit,
    ROUND(
        (total_profit / total_sales) * 100,
        2) AS profit_margin_pct

FROM category_profitability

ORDER BY
    profit_margin_pct DESC;

/*
Business Insight:

Profit margin highlights which categories
retain the largest proportion of revenue
after covering product costs.
*/

-- ============================================================
-- Profitability Analysis 4
-- Average Profit per Order
--
-- Business Question:
-- On average, how much profit
-- does each completed order generate?
-- ============================================================

SELECT
    ROUND(
        SUM(od.line_profit)
        /
        COUNT(DISTINCT o.order_id),
        2
    ) AS average_profit_per_order

FROM orders o

JOIN order_details od
ON o.order_id = od.order_id

WHERE
    o.order_status <> 'Cancelled';

/*
Business Insight:

Average profit per order provides a useful
benchmark for evaluating pricing strategies
and sales performance over time.
*/

-- ============================================================
-- Profitability Analysis 5
-- Profit by Order Source
--
-- Business Question:
-- Which sales channels generate
-- the highest profit?
-- ============================================================

SELECT
    o.order_source,
    ROUND(
        SUM(od.line_profit),
        2
    ) AS total_profit,
    ROUND(
        (SUM(od.line_profit) / SUM(od.line_total))
        * 100,
        2
    ) AS profit_margin_pct

FROM orders o

JOIN order_details od
ON o.order_id = od.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    o.order_source
ORDER BY
    total_profit DESC;

/*
Business Insight:

Comparing profitability across sales channels
helps identify where revenue translates into
the strongest financial returns.
*/

-- ============================================================
-- Profitability Analysis 6
-- Highest Product Profit Margin
--
-- Business Question:
-- Which products achieve the
-- highest average profit margin?
-- ============================================================

SELECT
    p.product_name,
    ROUND(
        AVG(
            (od.line_profit / od.line_total)
            * 100
        ),
        2
    ) AS average_profit_margin_pct

FROM products p

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    p.product_name
ORDER BY
    average_profit_margin_pct DESC
LIMIT 10;

/*
Business Insight:

High-margin products may deserve increased
marketing attention because they generate
more profit for each peso of sales revenue.
*/