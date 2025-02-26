WITH ordered_orders AS (
  SELECT 
    BuyerId,
    CreatedAt,
    ROW_NUMBER() OVER (PARTITION BY BuyerId ORDER BY CreatedAt) AS order_num,
    LAG(CreatedAt) OVER (PARTITION BY BuyerId ORDER BY CreatedAt) AS prev_order_date
  FROM Orders
  WHERE Cancelled = 'FALSE'
)
SELECT 
  AVG(JULIANDAY(CreatedAt) - JULIANDAY(prev_order_date)) AS avg_interval_days
FROM ordered_orders
WHERE order_num BETWEEN 2 AND 10;
