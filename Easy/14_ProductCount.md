**Problem Statement:**
You are provided with a table that lists various product categories, each containing a comma-separated list of products. 
Your task is to write a SQL query to count the number of products in each category. Sort the result by product count.


**Output:**
| category    | product_count |
|-------------|---------------|
| Furniture   |             1 |
| Groceries   |             2 |
| Electronics |             3 |
| Clothing    |             4 |

```
select 
category,
LENGTH(products) - LENGTH(REPLACE(products, ',', '')) + 1 AS product_count 
from categories
ORDER BY product_count;
```
