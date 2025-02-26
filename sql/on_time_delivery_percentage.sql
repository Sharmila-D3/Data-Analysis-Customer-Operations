SELECT 
    o.field4 AS region,
    ROUND(
        100.0 * SUM(CASE WHEN TRIM(UPPER(d.field3)) = 'ON TIME' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS on_time_delivery_percentage
FROM orders1 o
JOIN delivery_performance d ON o.field1 = d.field1
GROUP BY o.field4;
