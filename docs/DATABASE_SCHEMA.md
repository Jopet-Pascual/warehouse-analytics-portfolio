# Database Schema

## Overview

This project uses a relational PostgreSQL database designed to support warehouse operations, sales transactions, inventory management, customer management, supplier management, and business reporting.

The database follows a normalized relational structure where each business entity is stored in its own table and linked through primary and foreign keys. This design minimizes data redundancy while maintaining referential integrity between related tables.

The database is built from validated datasets that have been cleaned and verified before import into PostgreSQL.

---

## Entity Relationship Diagram

```text
                         ┌──────────────────────┐
                         │      Suppliers       │
                         │   supplier_id (PK)   │
                         └──────────┬───────────┘
                                    │
                                    │ 1 : *
                                    ▼
                         ┌──────────────────────┐
                         │       Products       │
                         │   product_id (PK)    │
                         │   supplier_id (FK)   │
                         └───────┬───────┬──────┘
                                 │       │
                         1 : 1   │       │ 1 : *
                                 ▼       ▼
                    ┌──────────────┐  ┌──────────────────────┐
                    │  Inventory   │  │    Order Details     │
                    │ inventory_id │  │ order_detail_id (PK) │
                    │ product_id FK│  │ order_id (FK)        │
                    └──────────────┘  │ product_id (FK)      │
                                      └──────────┬───────────┘
                                                 │
                                                 │ * : 1
                                                 ▼
                                      ┌──────────────────────┐
                                      │        Orders        │
                                      │    order_id (PK)     │
                                      │    customer_id (FK)  │
                                      │    sales_rep_id (FK) │
                                      └───────┬─────────┬────┘
                                              │         │
                                       * : 1 │         │ * : 1
                                              ▼         ▼
                              ┌──────────────────┐  ┌──────────────────┐
                              │    Customers     │  │    Employees     │
                              │ customer_id (PK) │  │ employee_id (PK) │
                              └──────────────────┘  │ manager_id (FK)  │
                                                    └────────┬─────────┘
                                                             │
                                                             │ * : 1
                                                             │
                                                             ▼
                                                    ┌──────────────────┐
                                                    │    Employees     │
                                                    │  (Manager)       │
                                                    │ employee_id (PK) │
                                                    └──────────────────┘
```

> **Note**
>
> The `warehouse_id` column exists only in the `inventory` table and is intentionally stored as a regular attribute rather than a foreign key because this project does not include a separate warehouse master table.

---

# Tables

## Suppliers

**Purpose**

Stores supplier information for products maintained by the warehouse.

**Primary Key**

* `supplier_id`

**Referenced By**

* `products.supplier_id`

---

## Products

**Purpose**

Stores the master list of products available for sale and inventory management.

**Primary Key**

* `product_id`

**Foreign Keys**

* `supplier_id` → `suppliers.supplier_id`

**Referenced By**

* `order_details.product_id`
* `inventory.product_id`

---

## Customers

**Purpose**

Stores customer information used when recording sales transactions.

**Primary Key**

* `customer_id`

**Referenced By**

* `orders.customer_id`

---

## Employees

**Purpose**

Stores employee information for sales representatives, warehouse personnel, and management.

The table also supports the organizational reporting structure through a self-referencing manager relationship.

**Primary Key**

- `employee_id`

**Foreign Keys**

- `manager_id` → `employees.employee_id` *(Self-referencing)*

**Referenced By**

- `orders.employee_id`
---

## Orders

**Purpose**

Stores customer sales orders.

Each order represents a single customer transaction and may contain one or more products through the Order Details table.

**Primary Key**

* `order_id`

**Foreign Keys**

* `customer_id` → `customers.customer_id`
* `employee_id` → `employees.employee_id`

**Referenced By**

* `order_details.order_id`

---

## Order Details

**Purpose**

Stores the individual products belonging to each customer order.

This table resolves the one-to-many relationship between orders and products.

**Primary Key**

* `order_detail_id`

**Foreign Keys**

* `order_id` → `orders.order_id`
* `product_id` → `products.product_id`

---

## Inventory

**Purpose**

Stores inventory quantities and stock information for each product.

Inventory is maintained separately from the product master data to support inventory analysis and stock management.

**Primary Key**

* `inventory_id`

**Foreign Keys**

* `product_id` → `products.product_id`

**Additional Attribute**

* `warehouse_id` (Not implemented as a foreign key)

---

# Relationship Summary

| Parent Table | Child Table              | Relationship                     |
| ------------ | ------------------------ | -------------------------------- |
| Suppliers    | Products                 | One-to-Many                      |
| Products     | Inventory                | One-to-One                      |
| Customers    | Orders                   | One-to-Many                      |
| Employees    | Orders                   | One-to-Many                      |
| Employees    | Employees (`manager_id`) | One-to-Many *(Self-referencing)* |
| Orders       | Order Details            | One-to-Many                      |
| Products     | Order Details            | One-to-Many                      |

---

# Design Decisions

## Normalized Structure

Each business entity is stored in its own table to minimize redundancy and improve data consistency.

## Orders and Order Details

Orders and Order Details are separated to allow a single customer order to contain multiple products. This structure reflects a common transactional database design used in ERP and warehouse management systems.

## Product Master Data

Product information is maintained separately from transactional data so that product attributes are stored only once and referenced wherever needed.

## Inventory Management

Inventory is maintained in a dedicated table to separate stock information from product master data.

The `warehouse_id` column is stored as a regular attribute because the project models inventory at the warehouse level without implementing a separate warehouse master table.

## Supplier Management

Products reference suppliers through a foreign key relationship, allowing multiple products to be associated with the same supplier.

## Customer and Employee Relationships

Orders reference both customers and employees to identify who placed the order and which employee processed the transaction.

This design supports customer analysis, employee performance analysis, and sales reporting.

## Employee Hierarchy

The Employees table includes a self-referencing `manager_id` foreign key that links an employee to their direct manager.

This design models the organizational hierarchy without requiring a separate managers table, allowing each manager to supervise multiple employees while each employee reports to a single manager.
