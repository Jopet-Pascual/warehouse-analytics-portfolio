# Data Dictionary

This document describes every dataset included in the Warehouse Analytics Portfolio.

---

# suppliers.csv

Contains the master list of suppliers providing products to LOTS Corp.

## Primary Key

supplier_id

## Business Rules

The following business rules govern the `suppliers` table and are enforced through PostgreSQL constraints where applicable.

### Identification

- Every supplier must have a unique supplier ID.
- Every supplier must have a supplier name.
- Every supplier must have one contact person.

### Contact Information

- Every supplier must have a valid contact email.
- Every supplier must have a valid mobile number.
- Every supplier must have a complete business address consisting of street address, city, province, region, and country.

### Business Information

- Every supplier must have one payment term.
- Lead time represents the expected number of days before goods are delivered.
- Lead time cannot be negative.
- A supplier must be either **Active** or **Inactive**.

### Audit Information

- Every supplier record must contain a creation date.
- Every supplier record must contain a last updated date.
- A supplier record cannot be updated before it is created.

| Business Rule                                      | PostgreSQL Implementation                          |
| -------------------------------------------------- | -------------------------------------------------- |
| Every supplier has a unique supplier ID.           | `PRIMARY KEY (supplier_id)`                        |
| Every supplier must have a supplier name.          | `NOT NULL`                                         |
| Every supplier must have one contact person.       | `NOT NULL`                                         |
| Every supplier must have one email.                | `NOT NULL`                                         |
| Every supplier must have one mobile number.        | `NOT NULL`                                         |
| Every supplier must have one complete address.     | `NOT NULL` on address fields                       |
| Every supplier has one payment term.               | `NOT NULL`                                         |
| Lead time cannot be negative.                      | `CHECK (lead_time_days >= 0)`                      |
| Supplier status must be Active or Inactive.        | `CHECK (supplier_status IN ('Active','Inactive'))` |
| Every supplier record has a creation date.         | `NOT NULL`                                         |
| Every supplier record has an update date.          | `NOT NULL`                                         |
| A supplier cannot be updated before it is created. | `CHECK (updated_at >= created_at)`                 |

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| supplier_id | Text | Unique identifier for each supplier. |
| supplier_name | Text | Official supplier company name. |
| contact_person | Text | Primary supplier representative. |
| email | Text | Supplier email address. |
| mobile_number | Text | Supplier contact number. |
| street_address | Text | Supplier street address. |
| city | Text | Supplier city. |
| province | Text | Supplier province. |
| region | Text | Supplier region. |
| country | Text | Supplier country. |
| payment_terms | Text | Agreed payment terms (e.g., Net 30). |
| lead_time_days | Integer | Expected delivery lead time in days. |
| supplier_status | Text | Current supplier status (Active / Inactive). |
| created_at | Date | Record creation date. |
| updated_at | Date | Most recent record update date. |


# products.csv

Contains the product catalog sold by LOTS Corp.

## Primary Key

product_id

## Foreign Keys

supplier_id → suppliers.supplier_id

## Business Rules

The following business rules govern the `products` table and are enforced through PostgreSQL constraints where applicable.

### Identification

- Every product must have a unique product ID.
- Every product must have a unique SKU.
- Every product must belong to exactly one supplier.

### Product Information

- Every product must have a product name.
- Every product must belong to one product family.
- Every product must have one variant.
- Every product must belong to one brand.
- Every product must belong to one category.
- Every product must include a description.

### Pricing

- Cost price cannot be negative.
- Selling price cannot be negative.
- Selling price must be greater than or equal to the cost price.

### Inventory

- Reorder level cannot be negative.

### Product Status

- Every product is either **Active** or **Inactive**.

### Audit Information

- Every product record must contain a launch date.
- Every product record must contain a creation date.
- Every product record must contain a last updated date.
- A product record cannot be updated before it is created.

| Business Rule                                   | PostgreSQL Implementation             |
| ----------------------------------------------- | ------------------------------------- |
| Every product has a unique ID.                  | `PRIMARY KEY (product_id)`            |
| Every product belongs to one supplier.          | `FOREIGN KEY (supplier_id)`           |
| Product name is required.                       | `NOT NULL`                            |
| Product family is required.                     | `NOT NULL`                            |
| Variant is required.                            | `NOT NULL`                            |
| Brand is required.                              | `NOT NULL`                            |
| Category is required.                           | `NOT NULL`                            |
| Description is required.                        | `NOT NULL`                            |
| SKU is required.                                | `NOT NULL`                            |
| Cost price cannot be negative.                  | `CHECK (cost_price >= 0)`             |
| Selling price cannot be negative.               | `CHECK (selling_price >= 0)`          |
| Selling price must be at least the cost price.  | `CHECK (selling_price >= cost_price)` |
| Reorder level cannot be negative.               | `CHECK (reorder_level >= 0)`          |
| Product must be active or inactive.             | `BOOLEAN NOT NULL` (`active`)         |
| Product cannot be updated before it is created. | `CHECK (updated_at >= created_at)`    |


## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| product_id | Text | Unique product identifier. |
| product_name | Text | Product name including variant. |
| product_family | Text | Product family or model line. |
| variant | Text | Product variant or specification. |
| brand | Text | Product brand. |
| category | Text | Product category. |
| description | Text | Product description. |
| sku | Text | Stock Keeping Unit. |
| supplier_id | Text | Supplier providing the product. |
| cost_price | Decimal | Product acquisition cost. |
| selling_price | Decimal | Product selling price. |
| reorder_level | Integer | Minimum inventory level before replenishment. |
| active | Boolean | Indicates whether the product is active for sale. |
| launch_date | Date | Product launch date. |
| created_at | Date | Record creation date. |
| updated_at | Date | Most recent record update date. |


# customers.csv

### Business Purpose

Stores the master list of customers served by LOTS Corp. This table represents organizations that purchase products from the company and is used for customer analytics, sales reporting, order generation, customer segmentation, and account management.

## Primary Key

customer_id

## Business Rules

The following business rules govern the `customers` table and are enforced through PostgreSQL constraints where applicable.

### Identification

- Every customer must have a unique customer ID.
- Every customer must have a customer name.
- Every customer must belong to one customer type.

### Contact Information

- Every customer must have one contact person.
- Every customer must have a valid contact email.
- Every customer must have a valid mobile number.
- Every customer must have a business location consisting of city, province, and region.

### Business Information

- Every customer must belong to one industry.
- Credit limit cannot be negative.
- Payment terms must be specified.
- Every customer must be either **Active** or **Inactive**.

### Audit Information

- Every customer record must contain a creation date.
- Every customer record must contain a last updated date.
- A customer record cannot be updated before it is created.

| Business Rule | PostgreSQL Implementation |
|---------------|---------------------------|
| Every customer has a unique customer ID. | `PRIMARY KEY (customer_id)` |
| Customer name is required. | `NOT NULL` |
| Customer type is required. | `NOT NULL` |
| Contact person is required. | `NOT NULL` |
| Email is required. | `NOT NULL` |
| Mobile number is required. | `NOT NULL` |
| City is required. | `NOT NULL` |
| Province is required. | `NOT NULL` |
| Region is required. | `NOT NULL` |
| Credit limit cannot be negative. | `CHECK (credit_limit >= 0)` |
| Payment terms are required. | `NOT NULL` |
| Customer status must be Active or Inactive. | `CHECK (status IN ('Active','Inactive'))` |
| Creation date is required. | `NOT NULL` |
| Update date is required. | `NOT NULL` |
| Customer record cannot be updated before creation. | `CHECK (updated_at >= created_at)` |

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| customer_id | Text | Unique identifier for each customer. |
| customer_name | Text | Official customer or organization name. |
| customer_type | Text | Classification of the customer (e.g., Corporate, Government, Education, Healthcare, Retail). |
| industry | Text | Industry sector to which the customer belongs. |
| contact_person | Text | Primary contact person for the customer account. |
| email | Text | Customer email address. |
| mobile_number | Text | Customer contact number. |
| city | Text | Customer city. |
| province | Text | Customer province. |
| region | Text | Customer region. |
| credit_limit | Decimal | Maximum approved credit limit for the customer. |
| payment_terms | Text | Agreed payment terms (e.g., Net 30, Net 45, Net 60). |
| status | Text | Current customer status (Active or Inactive). |
| created_at | Date | Date the customer record was created. |
| updated_at | Date | Date the customer record was last updated. |


# employees.csv

### Business Purpose

Stores the master list of LOTS Corp. employees. This table represents the company's organizational structure and supports workforce reporting, management hierarchy, sales assignment, and operational analytics.

Sales Representatives are assigned to customer accounts and are responsible for all sales orders generated by those customers.

## Primary Key

employee_id

## Referenced By

sales_rep_id → orders.sales_rep_id

manager_id → employees.employee_id (Self-reference)

## Business Rules

The following business rules govern the `employees` table and are enforced through PostgreSQL constraints where applicable.

### Identification

- Every employee must have a unique employee ID.
- Every employee must have a first name.
- Every employee must have a last name.
- Every employee must have a full name.

### Employment Information

- Every employee must belong to one department.
- Every employee must have one job title.
- Every employee must have one employment type.
- Every employee reports to at most one manager.
- A manager must also be an employee.

### Contact Information

- Every employee must have a valid company email.
- Every employee must have a valid mobile number.

### Compensation

- Salary cannot be negative.

### Employment Status

- Every employee must be either **Active** or **Resigned**.

### Audit Information

- Every employee record must contain a hire date.
- Every employee record must contain a creation date time.
- Every employee record must contain a last updated date time.
- An employee record cannot be updated before it is created.

| Business Rule | PostgreSQL Implementation |
|---------------|---------------------------|
| Every employee has a unique employee ID. | `PRIMARY KEY (employee_id)` |
| Manager must also be an employee. | `FOREIGN KEY (manager_id)` (self-reference) |
| First name is required. | `NOT NULL` |
| Last name is required. | `NOT NULL` |
| Full name is required. | `NOT NULL` |
| Department is required. | `NOT NULL` |
| Job title is required. | `NOT NULL` |
| Email is required. | `NOT NULL` |
| Mobile number is required. | `NOT NULL` |
| Employment type is required. | `NOT NULL` |
| Salary cannot be negative. | `CHECK (salary >= 0)` |
| Employee status must be Active or Resigned. | `CHECK (status IN ('Active','Resigned'))` |
| Creation date is required. | `NOT NULL` |
| Update date is required. | `NOT NULL` |
| Employee record cannot be updated before creation. | `CHECK (updated_at >= created_at)` |

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| employee_id | Text | Unique identifier for each employee. |
| first_name | Text | Employee's first name. |
| last_name | Text | Employee's last name. |
| full_name | Text | Employee's complete name. |
| department | Text | Department where the employee is assigned. |
| job_title | Text | Employee's job position within the company. |
| manager_id | Text | Employee ID of the employee's direct manager. Top-level executives have no manager. |
| email | Text | Company email address. |
| mobile_number | Text | Employee contact number. |
| hire_date | Date | Employee date hired. |
| employment_type | Text | Employment classification (e.g., Regular, Probationary, Contract). |
| salary | Decimal | Employee monthly salary. |
| status | Text | Current employment status (Active or Resigned). |
| created_at | Datetime | Date with time the employee record was created. |
| updated_at | Datetime | Date with time the employee record was last updated. |

> **Design Note**
>
>The manager_id column is nullable to support top-level employees who do not report to another employee. When present, it references another record in the employees table, creating a self-referencing organizational hierarchy.
>
>Salary values represent monthly gross salary in Philippine Pesos (PHP).

# orders.csv

### Business Purpose

Stores the sales order transactions created by LOTS Corp. Each record represents a single customer order and serves as the header table for all sales transactions.

The table identifies **who placed the order, which Sales Representative handled the transaction, when the order occurred, and the current order and payment status**. Product-level details and financial calculations are stored separately in `order_details.csv`.

## Primary Key

order_id

## Foreign Keys

customer_id → customers.customer_id

sales_rep_id → employees.employee_id

## Referenced By

order_id → order_details.order_id

## Business Rules

The following business rules govern the `orders` table and are enforced through PostgreSQL constraints where applicable.

### Identification

- Every order must have a unique order ID.
- Every order must belong to exactly one customer.
- Every order must be handled by exactly one Sales Representative.

### Order Information

- Every order must have an order date.
- Every order must have an order status.
- Every order must have a payment status.

### Order Source

- Every order must have one order source.
- Valid order sources are **Sales Representative**, **Phone**, **Email**, **Walk-in**, and **Website**.

### Order Lifecycle

- An order may only have one current order status.
- Valid order statuses are **Processing**, **Shipped**, **Delivered**, **Cancelled**, and **Returned**.
- An order can only be returned after it has been delivered.
- A cancelled order cannot later become shipped or delivered.

### Payment

- Every order must have one payment status.
- Valid payment statuses are **Pending**, **Paid**, **Overdue**, **Refunded**, and **Cancelled**.
- A refunded payment normally indicates that money has been returned to the customer.
- A cancelled payment normally indicates that the associated order was cancelled before payment was completed or finalized.

### Audit Information

- Every order record must contain a creation timestamp.
- Every order record must contain a last updated timestamp.
- An order record cannot be updated before it is created.

| Business Rule | PostgreSQL Implementation |
|---------------|---------------------------|
| Every order has a unique order ID. | `PRIMARY KEY (order_id)` |
| Every order belongs to one customer. | `FOREIGN KEY (customer_id)` |
| Every order belongs to one Sales Representative. | `FOREIGN KEY (sales_rep_id)` |
| Order date is required. | `NOT NULL` |
| Order source is required. | `NOT NULL` |
| Order status is required. | `NOT NULL` |
| Payment status is required. | `NOT NULL` |
| Order status must be valid. | `CHECK (order_status IN ('Processing','Shipped','Delivered','Cancelled','Returned'))` |
| Payment status must be valid. | `CHECK (payment_status IN ('Pending','Paid','Overdue','Refunded','Cancelled'))` |
| Order source must be valid. | `CHECK (order_source IN ('Sales Representative','Phone','Email','Walk-in','Website'))` |
| Creation timestamp is required. | `NOT NULL` |
| Update timestamp is required. | `NOT NULL` |
| Order record cannot be updated before creation. | `CHECK (updated_at >= created_at)` |

> **Design Note**
>
> The PostgreSQL database validates individual attribute values (such as valid order statuses and payment statuses) using `CHECK` constraints. More complex business workflows—such as ensuring that a returned order must previously have been delivered or that a cancelled order cannot later become shipped—are documented as business rules but are not enforced through database constraints in this portfolio. These rules are typically implemented in the application layer or through workflow/business logic.

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| order_id | Text | Unique identifier for each sales order. |
| customer_id | Text | Customer who placed the order. |
| sales_rep_id | Text | Sales Representative responsible for the order. |
| order_date | Date | Date the order was placed. |
| order_status | Text | Current order status (e.g., Delivered, Shipped, Processing, Cancelled, Returned). |
| payment_status | Text | Current payment status (e.g., Paid, Refunded, Cancelled). |
| order_source | Text | Channel through which the order was received (e.g., Walk-in, Phone, Email, Website). |
| created_at | Datetime | Date with time the order record was created. |
| updated_at | Datetime | Date with time the order record was last updated. |

> **Design Note**
>
> The `orders.csv` table intentionally does not store order totals, costs, or profits. Financial metrics are calculated from the related records in `order_details.csv`, reducing data redundancy and following normalized database design principles.

# order_details.csv

### Business Purpose

Stores the line-item details for each sales order. Each record represents a single product purchased within an order and contains the quantity sold, pricing information, discounts, and profitability metrics.

This table is the primary source for sales analysis, revenue reporting, profitability analysis, product performance, and inventory consumption.

## Primary Key

order_detail_id

## Foreign Keys

order_id → orders.order_id

product_id → products.product_id

## Business Rules

The following business rules govern the `order_details` table and are enforced through PostgreSQL constraints where applicable.

### Identification

- Every order detail must have a unique order detail ID.
- Every order detail must belong to exactly one sales order.
- Every order detail must reference exactly one product.

### Product Information

- Every order detail must contain a quantity.
- Quantity must be greater than zero.
- Unit cost cannot be negative.
- Unit price cannot be negative.
- The selling price should be greater than or equal to the unit cost.

### Discounts

- Discount percentage cannot be negative.
- Discount percentage is stored as a decimal fraction.
- Discount percentage must be between 0.00 and 1.00.

### Financial Calculations

- Line total represents the net sales amount after discounts.
- Line cost represents the total cost of the sold quantity.
- Line profit represents the difference between line total and line cost.

### Audit Information

- Every order detail record must contain a creation timestamp.
- Every order detail record must contain a last updated timestamp.
- An order detail record cannot be updated before it is created.

| Business Rule | PostgreSQL Implementation |
|---------------|---------------------------|
| Every order detail has a unique ID. | `PRIMARY KEY (order_detail_id)` |
| Every order detail belongs to one order. | `FOREIGN KEY (order_id)` |
| Every order detail references one product. | `FOREIGN KEY (product_id)` |
| Quantity must be greater than zero. | `CHECK (quantity > 0)` |
| Unit cost cannot be negative. | `CHECK (unit_cost >= 0)` |
| Unit price cannot be negative. | `CHECK (unit_price >= 0)` |
| Selling price must be greater than or equal to unit cost. | `CHECK (unit_price >= unit_cost)` |
| Discount percentage must be between 0.00 and 1.00. | `CHECK (discount_pct BETWEEN 0 AND 100)` |
| Creation timestamp is required. | `NOT NULL` |
| Update timestamp is required. | `NOT NULL` |
| Order detail record cannot be updated before creation. | `CHECK (updated_at >= created_at)` |

> **Design Note**
>
> The `order_details` table stores financial values that were calculated during dataset generation. Although values such as `line_total`, `line_cost`, and `line_profit` can be derived from unit price, quantity, and discount, they are intentionally stored to preserve the financial snapshot at the time of sale and to simplify analytical reporting. PostgreSQL validates their mathematical consistency using `CHECK` constraints.

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| order_detail_id | Text | Unique identifier for each order line. |
| order_id | Text | Sales order associated with the line item. |
| product_id | Text | Product purchased in the order. |
| quantity | Integer | Number of units purchased. |
| unit_cost | Decimal | Cost per unit at the time of the sale. |
| unit_price | Decimal | Selling price per unit before discount. |
| discount_pct | Decimal | Discount percentage applied to the line item. |
| line_total | Decimal | Net sales amount after discount. |
| line_cost | Decimal | Total cost of the sold quantity. |
| line_profit | Decimal | Profit earned from the line item (Line Total − Line Cost). |
| created_at | Datetime | Date with time the order detail record was created. |
| updated_at | Datetime | Date with time the order detail record was last updated. |


> **Design Note**
>
> Financial values are calculated at the line-item level rather than the order level. This design allows accurate reporting of product-level sales, discounts, costs, and profitability while avoiding duplicated calculations across multiple products within the same order.


# inventory.csv

### Business Purpose

Stores the current inventory position of each product across LOTS Corp.'s warehouses. This table represents the latest stock snapshot and is used for inventory monitoring, warehouse reporting, stock availability analysis, and replenishment planning.

Inventory quantities are generated based on historical sales activity, product demand, and predefined inventory planning rules.

## Primary Key

inventory_id

## Foreign Keys

product_id → products.product_id

## Business Rules

The following business rules govern the `inventory` table and are enforced through PostgreSQL constraints where applicable.

### Identification

- Every inventory record must have a unique inventory ID.
- Every inventory record must belong to exactly one product.
- Every inventory record must belong to one warehouse.

### Inventory Quantities

- Current stock cannot be negative.
- Reserved stock cannot be negative.
- Available stock cannot be negative.
- Reserved stock cannot exceed the current stock.
- Available stock represents the quantity available for immediate sale after reserved stock has been deducted.

### Inventory Status

- Every inventory record must have one inventory status.
- Valid inventory statuses are **In Stock** and **Out of Stock**.

### Inventory Movement

- The last stock movement date may be empty for products that have not yet experienced any inventory movement.

### Audit Information

- Every inventory record must contain a creation date.
- Every inventory record must contain a last updated date.
- An inventory record cannot be updated before it is created.

| Business Rule | PostgreSQL Implementation |
|---------------|---------------------------|
| Every inventory record has a unique inventory ID. | `PRIMARY KEY (inventory_id)` |
| Every inventory record belongs to one product. | `FOREIGN KEY (product_id)` |
| Warehouse ID is required. | `NOT NULL` |
| Current stock cannot be negative. | `CHECK (current_stock >= 0)` |
| Reserved stock cannot be negative. | `CHECK (reserved_stock >= 0)` |
| Available stock cannot be negative. | `CHECK (available_stock >= 0)` |
| Reserved stock cannot exceed current stock. | `CHECK (reserved_stock <= current_stock)` |
| Inventory status must be valid. | `CHECK (inventory_status IN ('In Stock','Out of Stock'))` |
| Creation date is required. | `NOT NULL` |
| Update date is required. | `NOT NULL` |
| Inventory record cannot be updated before creation. | `CHECK (updated_at >= created_at)` |

> **Design Note**
>
> The `inventory` table stores the latest inventory snapshot for each product within a warehouse rather than maintaining a complete inventory transaction history. Historical inventory movements are represented only by the `last_stock_movement` date. The `last_stock_movement` column may contain `NULL` for products that have not yet experienced any inventory movement.

## Columns

| Column | Data Type | Description |
|---------|-----------|-------------|
| inventory_id | Text | Unique identifier for each inventory record. |
| product_id | Text | Product associated with the inventory record. |
| warehouse_id | Text | Identifier of the warehouse where the inventory is currently stored. In this portfolio, warehouse information is represented as a business attribute rather than a separate master table. |
| current_stock | Integer | Total quantity currently stored in the warehouse. |
| reserved_stock | Integer | Quantity reserved for pending customer orders. |
| available_stock | Integer | Quantity available for immediate sale after reserved stock is deducted. |
| inventory_status | Text | Current inventory condition (In Stock, or Out of Stock). |
| last_stock_movement | Date | Date of the most recent inventory movement derived from product sales activity. |
| created_at | Date | Date the inventory record was created. |
| updated_at | Date | Date the inventory record was last updated. |

> **Design Note**
>
> Inventory levels are not generated randomly. Current stock is estimated using historical sales volume, sales velocity, inventory coverage rules, and planning variance. This produces inventory levels that better resemble real business operations while maintaining realistic relationships between sales and stock availability.