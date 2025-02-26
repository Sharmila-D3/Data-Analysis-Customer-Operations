WITH order_diffs AS (
    SELECT 
        field2 AS customer_id,
        field3 AS order_date,
        julianday(field3) - julianday(LAG(field3) OVER (PARTITION BY field2 ORDER BY field3)) AS diff_days
    FROM orders1
)
SELECT 
    customer_id, 
    AVG(diff_days) AS avg_days_between_orders
FROM order_diffs
WHERE diff_days IS NOT NULL
GROUP BY customer_id;
