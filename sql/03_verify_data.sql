/*
===========================================================
LOTS Corp Warehouse Analytics
Verifying imported datasets to tables
===========================================================

Description:
Verifying the number of rows of every tables to make
sure the imported datasets are correct.

Author:
Jopet Pascual

Repository:
https://github.com/Jopet-Pascual/warehouse-analytics-portfolio
===========================================================
*/

-- ==========================================
-- Verify Row Counts
-- ==========================================

SELECT COUNT(*) AS suppliers
FROM suppliers;

SELECT COUNT(*) AS products
FROM products;

SELECT COUNT(*) AS customers
FROM customers;

SELECT COUNT(*) AS employees
FROM employees;

SELECT COUNT(*) AS orders
FROM orders;

SELECT COUNT(*) AS inventory
FROM inventory;

SELECT COUNT(*) AS order_details
FROM order_details;

-- ==========================================
-- Checking Products without Suppliers
-- ==========================================
SELECT COUNT(*) AS invalid_products
FROM products p
LEFT JOIN suppliers s
ON p.supplier_id = s.supplier_id
WHERE s.supplier_id IS NULL;

-- ==========================================
-- Checking Orders without Customers
-- ==========================================
SELECT COUNT(*) AS invalid_orders
FROM orders o
LEFT JOIN customers c
ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- =============================================
-- Checking Orders without Sales Representatives
-- =============================================
SELECT COUNT(*) AS invalid_sales_reps
FROM orders o
LEFT JOIN employees e
ON o.sales_rep_id = e.employee_id
WHERE e.employee_id IS NULL;

-- =============================================
-- Checking Inventory without Products
-- =============================================
SELECT COUNT(*) AS invalid_inventory
FROM inventory i
LEFT JOIN products p
ON i.product_id = p.product_id
WHERE p.product_id IS NULL;

-- =============================================
-- Checking Order Details without Orders
-- =============================================
SELECT COUNT(*) AS invalid_order_details
FROM order_details od
LEFT JOIN orders o
ON od.order_id = o.order_id
WHERE o.order_id IS NULL;

-- =============================================
-- Checking Order Details without Products
-- =============================================
SELECT COUNT(*) AS invalid_products
FROM order_details od
LEFT JOIN products p
ON od.product_id = p.product_id
WHERE p.product_id IS NULL;

-- =============================================
-- Checking Duplicate Primary Keys
-- =============================================
SELECT supplier_id,
       COUNT(*)
FROM suppliers
GROUP BY supplier_id
HAVING COUNT(*) > 1;

SELECT product_id,
       COUNT(*)
FROM products
GROUP BY product_id
HAVING COUNT(*) > 1;

SELECT customer_id,
       COUNT(*)
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT employee_id,
       COUNT(*)
FROM employees
GROUP BY employee_id
HAVING COUNT(*) > 1;

SELECT order_id,
       COUNT(*)
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;

SELECT inventory_id,
       COUNT(*)
FROM inventory
GROUP BY inventory_id
HAVING COUNT(*) > 1;

SELECT order_detail_id,
       COUNT(*)
FROM order_details
GROUP BY order_detail_id
HAVING COUNT(*) > 1;

/*
=========================================================
Verification Complete

Expected Results

✓ All row counts match the cleaned CSV files.

✓ No duplicate primary keys.

✓ No orphan foreign keys.

If all checks pass, the database is ready
for analytical SQL queries.
=========================================================
*/

