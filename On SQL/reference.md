# SQL Reference

## Contents

- [BETWEEN](#between)
- [Common Table Expression](#common-table-expression)
- [COPY](#copy)
- [CREATE](#create)
- [DynamoDB PartiQL](#dynamodb-partiql)
- [EXISTS](#exists)
- [Indexes](#indexes)
- [Normalisation](#normalization)
- [Recursive CTE](#recursive-cte)
- [Table Size](#table-size)
- [Window Functions](#window-functions)

## BETWEEN

The values can be numbers, text, or dates.

Begin and end values are included. 

```sql
SELECT column_name
FROM table_name
WHERE column_name BETWEEN value1 AND value2; 
```

## Common Table Expression

Examples using [S3 http logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html) loaded into a PostgreSQL localhost

```sql
WITH my_cte AS (
    SELECT
        requestdatetime::DATE, 
        "key",
        SUM(REPLACE(bytessent, '''-', '0')::INT) AS bytessent
    FROM public.http_logs
    GROUP BY
        requestdatetime::DATE, 
        "key"
)
SELECT * FROM my_cte
```

## COPY

```sql
COPY my_table FROM 'D:\input.csv'
WITH QUOTE '"' CSV HEADER 
```

## CREATE

An example with SERIAL as an incremental integer and an inline primary key

```sql
CREATE TABLE my_table (
    my_pk SERIAL PRIMARY KEY,
    my_column VARCHAR(300)
)
```

An example with foreign keys and multi column primary key

```sql
CREATE TABLE my_table (
    my_first_id INT REFERENCES my_first_table(my_first_id),
    my_second_id INT REFERENCES my_second_table(my_second_id),
    my_metric INT,
    PRIMARY KEY (my_first_id, my_second_id)
)
```

## DynamoDB PartiQL

Examples using [S3 http logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html) loaded into DynamoDB. DynamoDB is a NoSQL database and only has support for a limited amount of SQL via [PartiQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.html).

This query will return records for a specific day and file

```sql
SELECT bucket_name, useragent, remoteip, referrer
FROM "all_lambda_s3logs"
WHERE BEGINS_WITH(requestdatetime, '2023-03-08')
AND "key" = 'index.html'
```

## EXISTS

```sql
SELECT DISTINCT
    column_1,
    column_2,
    column_3
FROM my_first_table
WHERE NOT EXISTS (
    SELECT 1
    FROM my_second_table
    WHERE my_first_table.column_1 = my_second_table.column_1
    AND my_first_table.column_2 = my_second_table.column_2
    AND my_first_table.column_3 = my_second_table.column_3
)
```

## Indexes

PostgreSQL automatically creates a unique index when a unique constraint or primary key is defined for a table

A single column index will be useful for optimising JOINs, WHERE and ORDER BY

```sql
CREATE INDEX my_index_name ON my_table (my_column);
```

or multi-column

```sql
CREATE INDEX my_index_name ON my_table (my_column_one, my_column_2);
```

will be useful when both columns are needed, with the left column being the main index. Multi column is good for multiple columns, but may be slower for single column use, especialy as columns move to the right of the index

## Normalisation
Three types of anomaly
- Insertion anomaly: An item cannot be added as a dimension without a fact
- Update anomaly: The same information can be found in multiple rows. If not all rows are updated there can be multiple versions of the same information
- Deletion anomaly: Similar to insertion, if all facts for a certain dimension are removed, the dimension is removed

### Normal Form One
In the First normal form each field contains a single value

### Normal Form Six
The row contains the Primary Key, and at most one other attribute

## Recursive CTE

```sql
WITH RECURSIVE cte_name AS (
    SELECT id, name, parent_id
    FROM my_table
    WHERE parent_id = 6
    UNION ALL
    SELECT my_table.id, my_table.name, my_table.parent_id
    FROM my_table INNER JOIN cte_name
    ON cte_name.id = my_table.parent_id
)
SELECT * FROM cte_name;
```

## Table Size

For PostgreSQL

```sql
SELECT PG_SIZE_PRETTY(PG_RELATION_SIZE('my_table'))
```

## Window Functions

Examples using [S3 http logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html) loaded into a PostgreSQL localhost

Standard aggregation
```sql
SELECT
    requestdatetime::DATE, 
    "key",
    REPLACE(bytessent, '''-', '0')::INT,
    AVG(REPLACE(bytessent, '''-', '0')::INT) OVER (PARTITION BY requestdatetime::date),
    SUM(REPLACE(bytessent, '''-', '0')::INT) OVER (PARTITION BY requestdatetime::date)
FROM public.http_logs
```

Examples with RANK and ROW_NUMBER
```sql
SELECT 
    requestdatetime::DATE, 
    "key",
    REPLACE(bytessent, '''-', '0')::INT,
    RANK() OVER (PARTITION BY requestdatetime::DATE ORDER BY REPLACE(bytessent, '''-', '0')::INT DESC),
    ROW_NUMBER() OVER (PARTITION BY requestdatetime::DATE ORDER BY REPLACE(bytessent, '''-', '0')::INT DESC)
FROM public.http_logs
```