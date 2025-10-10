**Problem Statement:**

You are provided with two tables: Products and Sales. The Products table contains information about various products, including their IDs, names, and prices. 
The Sales table contains data about sales transactions, including the product IDs, quantities sold, and dates of sale. 
Your task is to write a SQL query to find the total sales amount for each product. 
Display product name and total sales . Sort the result by product name.

```
SELECT 
p.product_name,
SUM(p.price * s.quantity) AS total_sales_amount
FROM products p
JOIN sales s
ON p.product_id = s.product_id
GROUP BY p.product_name
ORDER BY p.product_name
```
