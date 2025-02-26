WITH customer_spend AS (
    SELECT 
        field2 AS customer_id, 
        SUM(field5) AS total_spend,
        COUNT(field1) AS order_count
    FROM orders1
    GROUP BY field2
),
percentile_threshold AS (
    SELECT 
        total_spend
    FROM customer_spend
    ORDER BY total_spend DESC
    LIMIT 1 OFFSET (SELECT CAST(0.9 * COUNT(*) AS INT) FROM customer_spend) - 1
)
SELECT 
    customer_id,
    total_spend,
    order_count,
    ROUND(total_spend * 1.0 / order_count, 2) AS avg_order_value
FROM customer_spend
WHERE total_spend >= (SELECT total_spend FROM percentile_threshold)
