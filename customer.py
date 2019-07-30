DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  customerNumber int(11) NOT NULL,
  customerName varchar(50) NOT NULL,
  contactLastName varchar(50) NOT NULL,
  contactFirstName varchar(50) NOT NULL,
  phone varchar(50) NOT NULL,
  addressLine1 varchar(50) NOT NULL,
  addressLine2 varchar(50) DEFAULT NULL,
  cit varchar(50) NOT NULL,
  state varchar(50) DEFAULT NULL,
  postalCode varchar(15) DEFAULT NULL,
  country varchar(50) NOT NULL,
  salesRepEmployeeNumber int(11) DEFAULT NULL,
  creditLimit decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (customerNumber),
  KEY salesRepEmployeeNumber (salesRepEmployeeNumber),
  FOREIGN KEY (salesRepEmployeeNumber) REFERENCES employees (employeeNumber)
);







DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
  employeeNumber int(11) NOT NULL,
  lastName varchar(50) NOT NULL,
  firstName varchar(50) NOT NULL,
  extensio varchar(10) NOT NULL,
  email varchar(100) NOT NULL,
  officeCode varchar(10) NOT NULL,
  reportsTo int(11) DEFAULT NULL,
  jobTitle varchar(50) NOT NULL,
  PRIMARY KEY (employeeNumber),
  KEY reportsTo (reportsTo),
  KEY officeCode (officeCode),
  FOREIGN KEY (reportsTo) REFERENCES employees (employeeNumber),
  FOREIGN KEY (officeCode) REFERENCES offices (officeCode)
);




DROP TABLE IF EXISTS offices;

CREATE TABLE offices (
  officeCode varchar(10) NOT NULL,
  city varchar(50) NOT NULL,
  phone varchar(50) NOT NULL,
  addressLine1 varchar(50) NOT NULL,
  addressLine2 varchar(50) DEFAULT NULL,
  state varchar(50) DEFAULT NULL,
  country varchar(50) NOT NULL,
  postalCode varchar(15) NOT NULL,
  territory varchar(10) NOT NULL,
  PRIMARY KEY (officeCode)
);




DROP TABLE IF EXISTS orderdetails;

CREATE TABLE orderdetails (
  orderNumber int(11) NOT NULL,
  productCode varchar(15) NOT NULL,
  quantityOrdered int(11) NOT NULL,
  priceEach decimal(10,2) NOT NULL,
  orderLineNumber smallint(6) NOT NULL,
  PRIMARY KEY (orderNumber,productCode),
  KEY productCode (productCod),
  FOREIGN KEY (orderNumber) REFERENCES orders (orderNumber),
  FOREIGN KEY (productCode) REFERENCES products (productCode)
);


DROP TABLE IF EXISTS orders;

use sales;
CREATE TABLE IF NOT EXISTS customers( 
   customer_id INT AUTO_INCREMENT PRIMARY KEY,
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255)NOT NULL,
   phone INT(40) NOT NULL,
   email VARCHAR(40) NOT NULL,
   street VARCHAR(50) NOT NULL, 
   city VARCHAR(50) NOT NULL,
   state VARCHAR(25) NOT NULL,
   zip_code INT(10) NOT NULL
   
);
CREATE TABLE IF NOT EXISTS orders( 
   order_id INT NOT NULL,
   customer_id INT NOT NULL,
   order_status VARCHAR(255) NOT NULL,
   order_date DATE NOT NULL,
   required_date DATE NOT NULL,
   shipped_date DATE NOT NULL, 
   store_id INT(50) NOT NULL,
   staff_id INT(10) NOT NULL, 
   FOREIGN KEY (customer_id)
   REFERENCES customers(customer_id)
);
CREATE TABLE IF NOT EXISTS staffs( 
   staff_id INT NOT NULL,
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255)NOT NULL,
   email VARCHAR(40) NOT NULL,
   phone INT(40) NOT NULL,
   acive VARCHAR(50) NOT NULL, 
   store_id INT(50) NOT NULL,
   manager_id INT(10) NOT NULL, 
   FOREIGN KEY (customer_id)
   REFERENCES customers(customer_id)
);
CREATE TABLE IF NOT EXISTS stores( 
   store_id INT NOT NULL,
   store_name VARCHAR(255) NOT NULL,
   phone INT(40) NOT NULL,
   email VARCHAR(40) NOT NULL,
   street VARCHAR(50) NOT NULL, 
   city VARCHAR(50) NOT NULL,
   state VARCHAR(25) NOT NULL,
   zip_code INT(10) NOT NULL,
   FOREIGN KEY (customer_id)
   REFERENCES customers(customer_id)
);
CREATE TABLE IF NOT EXISTS order_items( 
   order_id INT NOT NULL,
   item_id INT NOT NULL,
   product_id INT NOT NULL,
   

   FOREIGN KEY (customer_id)
   REFERENCES customers(customer_id)
);