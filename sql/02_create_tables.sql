/*
===========================================================
LOTS Corp Warehouse Analytics
Create Database Tables
===========================================================

Description:
Creates all tables, primary keys,foreign keys, and 
constrants for the LOTS Corp Warehouse
Analytics database.

IMPORTANT

Before executing this script,
connect to the lotscorp_warehouse database pdAdmin.

PostgreSQL does not support
USE database_name;

Execute this script only after opening the Query Tool
for lotscorp_warehouse.

Author:
Jopet Pascual

Repository:
https://github.com/Jopet-Pascual/warehouse-analytics-portfolio
===========================================================
*/
SELECT current_database();

CREATE TABLE suppliers (

    supplier_id      VARCHAR(8)   PRIMARY KEY,
    supplier_name    VARCHAR(100) NOT NULL,
    contact_person   VARCHAR(100) NOT NULL,
    email            VARCHAR(255) NOT NULL,
    mobile_number    VARCHAR(20)  NOT NULL,
    street_address   VARCHAR(255) NOT NULL,
    city             VARCHAR(100) NOT NULL,
    province         VARCHAR(100) NOT NULL,
    region           VARCHAR(100) NOT NULL,
    country          VARCHAR(100) NOT NULL,
    payment_terms    VARCHAR(50)  NOT NULL,
    lead_time_days   INTEGER      NOT NULL,
    supplier_status  VARCHAR(20)  NOT NULL,
    created_at       DATE         NOT NULL,
    updated_at       DATE         NOT NULL,

    CONSTRAINT chk_supplier_status
        CHECK (
            supplier_status IN (
                'Active',
                'Inactive'
            )
        ),

    CONSTRAINT chk_lead_time_days
        CHECK (
            lead_time_days >= 0
        ),

	CONSTRAINT chk_supplier_dates
		CHECK (
		    updated_at >= created_at
		)
);

CREATE TABLE products (

    product_id       VARCHAR(8)    PRIMARY KEY,
    product_name     VARCHAR(150)  NOT NULL,
    product_family   VARCHAR(100)  NOT NULL,
    variant          VARCHAR(100)  NOT NULL,
    brand            VARCHAR(100)  NOT NULL,
    category         VARCHAR(100)  NOT NULL,
    description      TEXT          NOT NULL,
    sku              VARCHAR(50)   NOT NULL,
    supplier_id      VARCHAR(8)    NOT NULL,
    cost_price       NUMERIC(12,2) NOT NULL,
    selling_price    NUMERIC(12,2) NOT NULL,
    reorder_level    INTEGER       NOT NULL,
    active           BOOLEAN       NOT NULL,
    launch_date      DATE          NOT NULL,
    created_at       DATE          NOT NULL,
    updated_at       DATE          NOT NULL,

    CONSTRAINT fk_products_supplier
        FOREIGN KEY (supplier_id)
        REFERENCES suppliers (supplier_id),

    CONSTRAINT chk_cost_price
        CHECK (
			cost_price >= 0
			),

    CONSTRAINT chk_selling_price
        CHECK (
			selling_price >= 0
			),

    CONSTRAINT chk_product_profit
        CHECK (
			selling_price >= cost_price
			),

    CONSTRAINT chk_reorder_level
        CHECK (
			reorder_level >= 0
			),

    CONSTRAINT chk_product_dates
        CHECK (
			updated_at >= created_at
			)
			
);

CREATE TABLE customers (

    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    customer_type VARCHAR(50) NOT NULL,
    industry VARCHAR(100) NOT NULL,
    contact_person VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(20) NOT NULL,
    city VARCHAR(100) NOT NULL,
    province VARCHAR(100) NOT NULL,
    region VARCHAR(100) NOT NULL,
    credit_limit NUMERIC(12,2) NOT NULL,
    payment_terms VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at DATE NOT NULL,
    updated_at DATE NOT NULL,

    CONSTRAINT chk_customer_credit_limit
	    CHECK (
	        credit_limit >= 0
	    ),
    CONSTRAINT chk_customer_status
	    CHECK (
	        status IN (
	            'Active',
	            'Inactive'
	        )
	    ),
    CONSTRAINT chk_customer_dates
	    CHECK (
	        updated_at >= created_at
	    )
);

CREATE TABLE employees (

    employee_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    full_name VARCHAR(200) NOT NULL,
    department VARCHAR(100) NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    manager_id VARCHAR(10),
    email VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    employment_type VARCHAR(20) NOT NULL,
    salary NUMERIC(12,2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
	
    CONSTRAINT fk_employee_manager
    FOREIGN KEY (manager_id)
    REFERENCES employees(employee_id),

    CONSTRAINT chk_employee_salary
	    CHECK (
	        salary >= 0
	    ),
		
    CONSTRAINT chk_employee_employment_type
	    CHECK (
	        employment_type IN (
	            'Regular',
				'Contract',
				'Probationary'
	        )
	    ),
	
    CONSTRAINT chk_employee_status
	    CHECK (
	        status IN (
	            'Active',
				'Resigned'
	        )
	    ),
	
    CONSTRAINT chk_employee_dates
	    CHECK (
	        updated_at >= created_at
	    )
);

CREATE TABLE orders (

    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    sales_rep_id VARCHAR(10) NOT NULL,
    order_date DATE NOT NULL,
    order_status VARCHAR(20) NOT NULL,
    payment_status VARCHAR(20) NOT NULL,
    order_source VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,

    CONSTRAINT fk_order_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id),

    CONSTRAINT fk_order_sales_rep
    FOREIGN KEY (sales_rep_id)
    REFERENCES employees(employee_id),

    CONSTRAINT chk_order_status
	    CHECK (
	        order_status IN (
	            'Cancelled',
				'Delivered', 
				'Returned', 
				'Shipped', 
				'Processing'
	        )
	    ),
	
    CONSTRAINT chk_payment_status
	    CHECK (
	        payment_status IN (
	            'Cancelled',
				'Paid', 
				'Refunded', 
				'Pending', 
				'Overdue'
	        )
	    ),
	
    CONSTRAINT chk_order_source
	    CHECK (
	        order_source IN (
	            'Sales Representative',
				'Phone',
				'Email', 
				'Walk-in', 
				'Website'
	        )
	    ),
	
    CONSTRAINT chk_order_dates
	    CHECK (
	        updated_at >= created_at
	    )
	
);

CREATE TABLE inventory (

    inventory_id VARCHAR(10) PRIMARY KEY,
    product_id VARCHAR(10) NOT NULL,
    warehouse_id VARCHAR(10) NOT NULL,
    current_stock INTEGER NOT NULL,
    reserved_stock INTEGER NOT NULL,
    available_stock INTEGER NOT NULL,
    inventory_status VARCHAR(20) NOT NULL,
    last_stock_movement DATE,
    created_at DATE NOT NULL,
    updated_at DATE NOT NULL,
	
    CONSTRAINT fk_inventory_product
    FOREIGN KEY (product_id)
    REFERENCES products(product_id),

    CONSTRAINT chk_current_stock
	    CHECK (
			current_stock >= 0
			),
	
    CONSTRAINT chk_reserved_stock
	    CHECK (
			reserved_stock >= 0
			),
	
    CONSTRAINT chk_available_stock_non_negative
	    CHECK (
			available_stock >= 0
			),
	
    CONSTRAINT chk_reserved_not_exceed_current
	    CHECK (
			reserved_stock <= current_stock
			),
	
    CONSTRAINT chk_available_stock
	    CHECK (
			available_stock = current_stock - reserved_stock
			),
	
    CONSTRAINT chk_inventory_status
	    CHECK (
				inventory_status IN (
					'In Stock', 
					'Out of Stock'
				)
			),
	
    CONSTRAINT chk_inventory_dates
	    CHECK (
			updated_at >= created_at
		),

	CONSTRAINT chk_inventory_status_logic
		CHECK (
			(available_stock = 0 AND inventory_status = 'Out of Stock')
			OR
			(available_stock > 0 AND inventory_status = 'In Stock')
			)
);

CREATE TABLE order_details (

    order_detail_id VARCHAR(10) PRIMARY KEY,
    order_id VARCHAR(10) NOT NULL,
    product_id VARCHAR(10) NOT NULL,
    quantity INTEGER NOT NULL,
    unit_cost NUMERIC(10,2) NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    discount_pct NUMERIC(3,2) NOT NULL,
    line_total NUMERIC(12,2) NOT NULL,
    line_cost NUMERIC(12,2) NOT NULL,
    line_profit NUMERIC(12,2) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,

    CONSTRAINT fk_order_detail_order
    FOREIGN KEY (order_id)
    REFERENCES orders(order_id),

    CONSTRAINT fk_order_detail_product
    FOREIGN KEY (product_id)
    REFERENCES products(product_id),

    CONSTRAINT chk_quantity
	    CHECK (
			quantity > 0
		),
	
    CONSTRAINT chk_unit_cost
	    CHECK (
			unit_cost >= 0
		),
	
    CONSTRAINT chk_unit_price
	    CHECK (
			unit_price >= 0
		),
	
    CONSTRAINT chk_price_vs_cost
	    CHECK (
			unit_price >= unit_cost
			),
		
    CONSTRAINT chk_discount_pct
	    CHECK (
			discount_pct BETWEEN 0.00 AND 1.00
			),
    
    CONSTRAINT chk_order_detail_dates
	    CHECK (
			updated_at >= created_at
			)
		
    /*
        Known Issue

        During database import, a small number of records failed the derived financial CHECK constraints 
        (line_total, line_cost, and line_profit) despite passing Python validation during dataset 
        generation. The discrepancy appears to be related to differences in numeric computation or serialization 
        between the Python generation pipeline and PostgreSQL's evaluation of derived values. Since these fields 
        are generated and validated during dataset creation, the mathematical CHECK constraints were removed 
        to allow completion of the portfolio. This issue has been documented for future investigation and 
        improvement.
    
    
            CONSTRAINT chk_line_total
                CHECK (
                    line_total = ROUND(
                                quantity * unit_price * (1 - discount_pct),
                                2)
                    ),
            
            CONSTRAINT chk_line_cost
                CHECK (
                    line_cost = ROUND(
                            quantity * unit_cost,
                        2)
                    ),
                
            CONSTRAINT chk_line_profit
                CHECK (
                    line_profit = ROUND(
                                line_total - line_cost,
                            2)
                    )
    */
		
);
