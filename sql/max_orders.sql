SELECT field2 AS customer_id, 
       MAX(field3) AS last_order_date, 
       COUNT(field1) AS order_count
FROM orders1
GROUP BY field2
HAVING MAX(field3) < date('now', '-60 days')
   AND COUNT(field1) >= 2;
