**Problem Statement:**

Write a query to find workaholics employees.  Workaholics employees are those who satisfy at least one of the given criterions:
 
- 1- Worked for more than 8 hours a day for at least 3 days in a week. 
2- worked for more than 10 hours a day for at least 2 days in a week. 
You are given the login and logout timings of all the employees for a given week. 
Write a SQL to find all the workaholic employees along with the criterion that they are satisfying (1,2 or both), display it in the order of increasing employee id

```
WITH CTE AS (
  select 
  *,
  TIMESTAMPDIFF(second, login, logout) / 3600.0,
  CASE
      WHEN TIMESTAMPDIFF(second, login, logout) / 3600.0 > 10 THEN '10+'
      WHEN TIMESTAMPDIFF(second, login, logout) / 3600.0 > 8 THEN '8+'
      ELSE '8-' 
  END AS time_window
  from employees
), 
time_window AS (
SELECT emp_id, 
COUNT(*) AS days_8,
SUM(CASE WHEN time_window = '10+' THEN 1 ELSE 0 END) AS days_10
FROM CTE
WHERE time_window IN ('10+', '8+')
GROUP BY emp_id)

 select emp_id, 
 case when days_8 >=3 and days_10>=2 then 'both'
	  when days_8 >=3 then '1'
 	  else '2' end as criterian
 from time_window
  where days_8>=3 or days_10>=2 
ORDER BY emp_id ASC;
```
