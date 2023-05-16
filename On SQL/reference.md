# SQL Reference

## Contents

- [COPY](#copy)
- [Recursive CTE](#recursive-cte)

## COPY

```sql
COPY my_table FROM 'D:\input.csv'
WITH QUOTE '"' CSV HEADER 
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