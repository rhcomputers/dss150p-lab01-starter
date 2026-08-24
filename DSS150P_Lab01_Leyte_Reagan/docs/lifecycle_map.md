# Data Engineering Lifecycle Map

## Lifecycle Elements

| Lifecycle Element | What It Means | Example in This Lab | Primary Tool/Artifact | Possible Failure |
|-------------------|---------------|---------------------|----------------------|------------------|
| Source system | Where data comes from | CSV, JSON, Parquet files, REST API | Raw data files | Files missing or corrupted |
| Ingestion/acquisition | Getting the data | pandas.read_csv(), requests.get() | Python scripts | Can't read files |
| Storage | Where data is stored | PostgreSQL database | Docker container | Database crashes |
| Processing/transformation | Changing data | Cleaning, profiling | Python with pandas | Wrong data types |
| Data quality/validation | Checking data | Null checks, duplicates | Python scripts | Bad data passes through |
| Delivery | Sending data | Exporting to database | SQL commands | Connection fails |
| Consumer | Who uses data | Analytics team | Reports/dashboards | Wrong data delivered |

## Data Flow Diagram

