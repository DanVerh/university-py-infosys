CREATE DATABASE db;

\c db

CREATE TABLE workers
(
    username VARCHAR(50) NOT NULL UNIQUE,
    user_password VARCHAR(8) NOT NULL
);

INSERT INTO workers (username, user_password) 
VALUES 
    ('productmanager', '12345678'),
    ('warehouseworker', '12345678'),
    ('salesmanager', '12345678'),
    ('logistician', '12345678'),
    ('accountant', '12345678');

CREATE TABLE products
( 
    product_name VARCHAR(50) PRIMARY KEY,
    price INT NOT NULL CHECK (price > 0),
    amount INT DEFAULT NULL
);

CREATE TABLE customers
( 
    customer_name VARCHAR(50) PRIMARY KEY,
    customer_address VARCHAR(50) NOT NULL
);

CREATE TABLE orders
( 
    order_id SERIAL PRIMARY KEY,
    product VARCHAR(50),
    amount INT NOT NULL CHECK (amount > 0),
    customer VARCHAR(50),
    sum INT,
    order_status INT DEFAULT 0 CHECK (order_status >= 0 AND order_status <=2),

    FOREIGN KEY (product) REFERENCES products(product_name) ON UPDATE NO ACTION,
    FOREIGN KEY (customer) REFERENCES customers(customer_name) ON UPDATE NO ACTION
);

