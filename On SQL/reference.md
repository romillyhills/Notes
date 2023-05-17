# SQL Reference

## Contents

- [Common Table Expression](#common-table-expression)
- [COPY](#copy)
- [DynamoDB PartiQL](#dynamodb-partiql)
- [Recursive CTE](#recursive-cte)
- [Window Functions](#window-functions)

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

## DynamoDB PartiQL

Examples using [S3 http logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html) loaded into DynamoDB. DynamoDB is a NoSQL database and only has support for a limited amount of SQL via [PartiQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.html).

This query will return records for a specific day and file

```sql
SELECT bucket_name, useragent, remoteip, referrer
FROM "all_lambda_s3logs"
WHERE BEGINS_WITH(requestdatetime, '2023-03-08')
AND "key" = 'index.html'
```

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