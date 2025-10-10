
**Problem Statement:**

You are a data analyst working for an e-commerce company, responsible for analysing customer orders to gain insights into their purchasing behaviour. 
Your task is to write a SQL query to retrieve the details of the penultimate order for each customer. 
However, if a customer has placed only one order, you need to retrieve the details of that order instead, display the output in ascending order of customer name.

| order_id | order_date | customer_name | product_name | sales |
|----------|------------|-------------|--------------|-------|
|        2 | 2023-01-02 | Alexa         | boAt         |   300 |
|        6 | 2023-01-03 | Neha          | Dress        |   100 |
|        4 | 2023-01-01 | Ramesh        | Titan        |   200 |

```
WITH cte AS (
    SELECT * 
         ,ROW_NUMBER() OVER(PARTITION BY customer_name ORDER BY order_date DESC) AS rn
  ,COUNT(*) OVER(PARTITION BY customer_name) AS cnt_of_orders
    FROM orders
)
SELECT 
    order_id,
    order_date,
    customer_name,
    product_name,
    sales
FROM cte
WHERE rn = 2 OR cnt_of_orders = 1
ORDER BY customer_name;
```
