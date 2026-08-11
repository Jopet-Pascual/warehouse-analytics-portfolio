-- ============================================================
-- View: vw_sales_summary
--
-- Business Purpose:
-- Provides an executive summary of sales,
-- cost, profit, and order performance.
-- ============================================================
CREATE OR REPLACE VIEW vw_sales_summary AS

WITH sales_summary AS (
    SELECT
        SUM(od.line_total) AS total_sales,
        SUM(od.line_cost) AS total_cost,
        SUM(od.line_profit) AS total_profit,
        COUNT(DISTINCT o.order_id) AS total_orders
		
    FROM orders o

    JOIN order_details od
    ON o.order_id = od.order_id

    WHERE
        o.order_status <> 'Cancelled'
)
SELECT
    ROUND(total_sales, 2) AS total_sales,
    ROUND(total_cost, 2) AS total_cost,
    ROUND(total_profit, 2) AS total_profit,
    ROUND(
        (total_profit / total_sales) * 100,
        2) AS profit_margin_pct,
    total_orders,
    ROUND(
        total_sales / total_orders,
        2) AS average_order_value

FROM sales_summary;

-- =============================
-- Test vw_sales_summary
-- =============================

SELECT *
FROM vw_sales_summary;

-- ============================================================
-- View: vw_product_performance
--
-- Business Purpose:
-- Summarizes sales performance for
-- every product.
-- ============================================================
CREATE OR REPLACE VIEW vw_product_performance AS

SELECT
    p.product_id,
    p.product_name,
    p.category,
    s.supplier_name,
    SUM(od.quantity) AS units_sold,
    ROUND(SUM(od.line_total),2) AS total_sales,
    ROUND(SUM(od.line_profit),2) AS total_profit,
    ROUND(AVG(od.discount_pct) * 100,2) AS average_discount_pct

FROM products p

JOIN suppliers s
ON p.supplier_id = s.supplier_id

JOIN order_details od
ON p.product_id = od.product_id

JOIN orders o
ON od.order_id = o.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    p.product_id,
    p.product_name,
    p.category,
    s.supplier_name;

-- =============================
-- Test vw_product_performance
-- =============================

SELECT *
FROM vw_product_performance
ORDER BY total_sales DESC;

-- ============================================================
-- View: vw_customer_performance
--
-- Business Purpose:
-- Summarizes purchasing performance
-- for every customer.
-- ============================================================

CREATE OR REPLACE VIEW vw_customer_performance AS

SELECT
    c.customer_id,
    c.customer_name,
    c.customer_type,
    c.industry,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(od.line_total),2) AS total_sales,
    ROUND(SUM(od.line_total)/COUNT(DISTINCT o.order_id),2) AS average_order_value

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN order_details od
ON o.order_id = od.order_id

WHERE
    o.order_status <> 'Cancelled'
GROUP BY
    c.customer_id,
    c.customer_name,
    c.customer_type,
    c.industry;

-- =============================
-- Test vw_customer_performance
-- =============================

SELECT *
FROM vw_customer_performance
ORDER BY total_sales DESC;

-- ============================================================
-- View: vw_inventory_status
--
-- Business Purpose:
-- Combines product master data with
-- current inventory information.
-- ============================================================

CREATE OR REPLACE VIEW vw_inventory_status AS

SELECT
    p.product_id,
    p.product_name,
    p.category,
    i.warehouse_id,
    i.current_stock,
    i.reserved_stock,
    i.available_stock,
    p.reorder_level,
    i.inventory_status,
    i.last_stock_movement

FROM products p

JOIN inventory i
ON p.product_id = i.product_id;

-- =============================
-- Test vw_inventory_status
-- =============================

SELECT *
FROM vw_inventory_status;

-- ============================================================
-- View: vw_supplier_performance
--
-- Business Purpose:
-- Summarizes supplier performance
-- using sales and product data.
-- ============================================================

CREATE OR REPLACE VIEW vw_supplier_performance AS

SELECT
    s.supplier_id,
    s.supplier_name,
    COUNT(DISTINCT p.product_id) AS total_products,
    ROUND(SUM(od.line_total),2) AS total_sales,
    ROUND(SUM(od.line_profit),2) AS total_profit,
    MAX(s.lead_time_days) AS suppplier_lead_time_days

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
    s.supplier_name;

-- =============================
-- Test vw_supplier_performance
-- =============================

SELECT *
FROM vw_supplier_performance
ORDER BY total_sales DESC;