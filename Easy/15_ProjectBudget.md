**Problem Statement:**
You are tasked with managing project budgets at a company. Each project has a fixed budget, and multiple employees work on these projects. 
The company's payroll is based on annual salaries, and each employee works for a specific duration on a project.
 
Over budget on a project is defined when the salaries (allocated on per day basis as per project duration) exceed the budget of the project. 
For example, if Ankit and Rohit both combined income make 200K and work on a project of a budget of 50K that takes half a year, then the project is over budget given 0.5 * 200K = 100K > 50K.

Write a query to forecast the budget for all projects and return a label of "overbudget" if it is over budget and "within budget" otherwise. Order the result by project title.

| title              | budget | label         |
|--------------------|--------|---------------|
| Analytics Platform |  80000 | within budget |
| App Development    | 100000 | overbudget    |
| Cloud Migration    |  20000 | overbudget    |
| Website Redesign   |  50000 | within budget |

```
WITH Project_Salary_Cost AS (
    SELECT 
        p.title AS project_title,
        p.budget,
        SUM(e.salary * (DATEDIFF(p.end_date, p.start_date) / 365.0)) AS total_salary_cost
  FROM 
        Projects p
    JOIN 
        Project_Employees pe ON p.id = pe.project_id
    JOIN 
        Employees e ON e.id = pe.employee_id
    GROUP BY 
        p.id, p.title, p.budget
)
SELECT 
    project_title AS title,
    budget,
    CASE 
        WHEN total_salary_cost > budget THEN 'overbudget'
        ELSE 'within budget'
    END AS label
FROM 
    Project_Salary_Cost                                                   
ORDER BY 
    project_title;                                                       
```
