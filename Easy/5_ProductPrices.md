**Problem Statement: **
You are given a products table where a new row is inserted every time the price of a product changes. Additionally, there is a transaction table containing details such as order_date and product_id for each order.
Write an SQL query to calculate the total sales value for each product, considering the cost of the product at the time of the order date, display the output in ascending order of the product_id.

| product_id | total_sales |
|-----------|-------------|
|        100 |         510 |
|        101 |        4700 |

```
WITH price_range AS (
    SELECT *,
           DATE_ADD(LEAD(price_date, 1, '9999-12-31') OVER (PARTITION BY product_id ORDER BY price_date), INTERVAL -1 DAY) AS price_end_date  --    Calculate price end date as one day before next price_date
    FROM products                                                                    --    Products table containing price history
)
SELECT 
p.product_id, 
SUM(p.price) AS total_sales
--    Sum total price for orders within valid price period
FROM orders o
INNER JOIN price_range p 
ON o.product_id = p.product_id
--    Join orders with price ranges on product_id
AND o.order_date BETWEEN p.price_date AND p.price_end_date
--    Filter orders within price validity period
GROUP BY p.product_id
--    Group by product_id to aggregate sales
ORDER BY p.product_id ASC;
```
