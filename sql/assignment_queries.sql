-- 1. Create Users Table
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    user_name TEXT,
    created_at TEXT
);

--insert values of the Users table
INSERT INTO Users (id, user_name, created_at) VALUES
(24280, 'Kayla Evans', '2023-03-06 23:42'),
(24603, 'Nichole Robinson', '2023-06-21 11:04'),
(24812, 'Amanda Luedtke', '2024-03-07 14:01'),
(25039, 'Cassandra Nelson', '2023-03-17 20:41'),
(25040, 'Deena Hougard', '2023-03-17 20:45'),
(25851, 'John Horihan', '2023-04-02 17:49'),
(25953, 'Katie Cvelbar', '2023-04-03 07:04');

-- 2. Create Orders Table
CREATE TABLE Orders (
    id INTEGER PRIMARY KEY,
    buyerid INTEGER,
    created_at TEXT,
    cancelled TEXT,
    FOREIGN KEY (buyerid) REFERENCES Users (id)
);

--insert values of the Orders table
INSERT INTO Orders (id, buyerid, created_at, cancelled) VALUES
(67507, 24280, '2023-03-08 23:42', 'FALSE'),
(67618, 25039, '2023-03-29 13:08', 'FALSE'),
(68660, 24603, '2023-07-05 09:09', 'TRUE'),
(68750, 24280, '2023-04-02 17:55', 'FALSE'),
(69645, 25851, '2023-04-07 16:01', 'TRUE'),
(70264, 24603, '2023-07-08 12:45', 'FALSE'),
(70390, 25953, '2023-04-10 10:28', 'FALSE');

-- 3. Query to Calculate Average Time Between Orders
WITH RankedOrders AS (
    SELECT
        buyerid,
        created_at,
        ROW_NUMBER() OVER (PARTITION BY buyerid ORDER BY datetime(created_at)) AS order_number
    FROM Orders
    WHERE cancelled = 'FALSE'
),
OrderDifferences AS (
    SELECT
        buyerid,
        created_at,
        order_number,
        LAG(created_at) OVER (PARTITION BY buyerid ORDER BY datetime(created_at)) AS previous_order_date
    FROM RankedOrders
    WHERE order_number <= 10
)
SELECT
    buyerid,
    AVG(julianday(created_at) - julianday(previous_order_date)) AS avg_days_between_orders
FROM OrderDifferences
WHERE previous_order_date IS NOT NULL
GROUP BY buyerid;
