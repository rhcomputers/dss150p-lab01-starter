# Source Systems Inventory

| Field | customers.csv | orders.json | products.parquet | API Snapshot |
|-------|---------------|-------------|------------------|--------------|
| Source name | Customers CSV | Orders JSON | Products Parquet | REST API |
| Source-system type | File system | File system | File system | Web API |
| Data format | CSV | JSON | Parquet | JSON |
| Structured/Semi-structured | Structured | Semi-structured | Structured | Semi-structured |
| Expected update pattern | Batch | Batch | Batch | On-demand |
| Likely acquisition method | File download | File download | File download | HTTP GET |
| Schema location | File header | Embedded data | Parquet schema | API response |
| Possible primary key | customer_id | order_id | product_id | id field |
| Schema-evolution risk | Low | Medium | Low | High |
| Data-quality risk | Null values | Missing fields | Null values | API downtime |

## API Snapshot

Retrieval timestamp (UTC): To be added when API script runs
