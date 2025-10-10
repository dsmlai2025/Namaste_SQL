**Problem Statement:**
You are provided with a table named Products containing information about various products, including their names and prices. Write a SQL query to count number of products in each category based on its price into three categories below. Display the output in descending order of no of products.
 
- 1- "Low Price" for products with a price less than 100
- 2- "Medium Price" for products with a price between 100 and 500 (inclusive)
- 3- "High Price" for products with a price greater than 500.

**Tables: Products**

| category     | no_of_products |
|--------------|----------------|
| Low Price    |              9 |
| Medium Price |              4 |
| High Price   |              2 |

```
select 
CASE WHEN price < 100 THEN 'Low Price'
	 WHEN price > 100 AND price < 500 THEN 'Medium Price'
     WHEN price > 500 THEN 'High Price'
END AS category,
COUNT(*) AS no_of_products
from products
GROUP BY category
ORDER BY no_of_products DESC;
```
