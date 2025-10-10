**Problem Statement:**

You own a small online store, and want to analyze customer ratings for the products that you're selling. After doing a data pull, you have a list of products and a log of purchases. Within the purchase log, each record includes the number of stars (from 1 to 5) as a customer rating for the product.
For each category, find the lowest price among all products that received at least one 4-star or above rating from customers. If a product category did not have any products that received at least one 4-star or above rating, the lowest price is considered to be 0. The final output should be sorted by product category in alphabetical order.

| category | price |
|----------|-------|
| apple    |     0 |
| cherry   |    36 |
| grape    |     0 |
| orange   |    14 |

```
SELECT 
    category,
    COALESCE(MIN(CASE WHEN pur.product_id IS NOT NULL THEN price END), 0) AS price
FROM products p
LEFT JOIN purchases pur 
ON p.id = pur.product_id AND pur.stars IN (4, 5)
GROUP BY category
ORDER BY category;
```
