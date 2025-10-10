**Problem Statement:**

Suppose you are a data analyst working for a retail company, and your team is interested in analysing customer feedback to identify trends and patterns in product reviews.
Your task is to write an SQL query to find all product reviews containing the word "excellent" or "amazing" in the review text. However, you want to exclude reviews that contain the word "not" immediately before "excellent" or "amazing". Please note that the words can be in upper or lower case or combination of both. 
Your query should return the review_id,product_id, and review_text for each review meeting the criteria, display the output in ascending order of review_id.

```
select 
* 
from product_reviews 
WHERE 
(LOWER(review_text) LIKE ('%excellent%') OR LOWER(review_text) LIKE ('%amazing%' ))
AND LOWER(review_text) NOT LIKE ('% not amazing%')
AND LOWER(review_text) NOT LIKE ('% not excellent%')
ORDER BY review_id ;
```
