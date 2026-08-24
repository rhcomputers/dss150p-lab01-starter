# My Reflection

## What I Learned

### Data Engineering Lifecycle
From this actvity I managed to learn how source systems, pipelines, storage, and consumers fit together. The lifecycle map actually helped me visualize how data moves from raw files to a database and finally to analysts.

### Environment Setup
I still have some confusions in this part, I don't know if I did it properly, after all, my Docker never worked at all. Every time I tried using the Docker in the Terminal it just always doesnt connect to it. I tried using .venv but it just crashed more so I just stopped.

### Data Profiling
I learned how to profile different data formats (CSV, JSON, Parquet) using pandas. Can be seen in my profile_sources in src, fun but also made me cry a bit, the coding is not that hard but I really should relearn python again.

### API Integration
I learned how to fetch data from REST APIs using the requests library.

### Challenges Faced
Coding is a challenge, the vacation realy made me forget some of the Python activites before, Docker is the biggest challenge, a challenge that I failed to conquer, I guess I have to fix it before the next lab activity.

## Data Quality Observations

### customers.csv
- customer_id appears to be a good primary key
- Some null values in email and phone fields

### orders.json
- Contains nested structures that need flattening
- Date fields stored as strings requiring conversion

### products.parquet
- Efficient storage format
- Consistent data types across all records

## What I Would Do Differently
I would test Docker earlier and ensure all prerequisites are met before starting the lab. I feel like I need to redownload this thing.