# Source Data Profile Analysis

## customers.csv

File: customers.csv
Rows: 250 | Columns: 7
Columns: customer_id, first_name, last_name, email, city, signup_date, customer_segment

Observations:
1. The file contains 250 customer records with 7 columns. The `customer_id` column has no null values (0 missing) and appears to be a good primary key for future joins.
2. There are 2 duplicate rows that would need to be removed before loading into a database. Data quality issues include 3 missing emails and 2 missing cities. The `signup_date` is stored as a string (object) and should be converted to datetime for time-based analysis.

---

## orders.json

File: orders.json
Rows: 250 | Columns: 9
Columns: order_id, customer_id, order_timestamp, status, item_count, subtotal, shipping_fee, total_amount, shipping

Observations:
1. The JSON file contains 250 order records with 9 fields. There are no null values across any columns, indicating good data quality.
2. The `shipping` column contains nested object data (dictionary) that cannot be processed in a simple tabular format. This nested structure would need to be flattened (extracted into separate columns) before loading into a relational database. Additionally, the `order_timestamp` is stored as a string and should be converted to datetime format.

---

## products.parquet

File: products.parquet
Rows: 200 | Columns: 7
Columns: product_id, product_name, category, brand, unit_price, stock_quantity, weight_kg

Observations:
1. The Parquet file contains 200 product records with 7 columns. There are zero null values and zero duplicate rows, making this the cleanest and most reliable data source.
2. The `product_id` column has no nulls and serves as a strong primary key. All numeric columns (`unit_price`, `stock_quantity`, `weight_kg`) have consistent data types and are ready for analysis.