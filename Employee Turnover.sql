--  Extracting data from the employee_churn_data dataset
SELECT 
*
FROM 
PortfolioProject.dbo.employee_churn_data

-- Null values in the dataset
SELECT 
SUM(CASE WHEN Department IS NULL THEN 1 ELSE 0 END) AS Null_Department,
SUM(CASE WHEN Promoted IS NULL THEN 1 ELSE 0 END) AS Null_Promoted,
SUM(CASE WHEN Review IS NULL THEN 1 ELSE 0 END) AS Null_Review,
SUM(CASE WHEN Projects IS NULL THEN 1 ELSE 0 END) AS Null_Projects,
SUM(CASE WHEN Salary IS NULL THEN 1 ELSE 0 END) AS Null_Salary,
SUM(CASE WHEN Tenure IS NULL THEN 1 ELSE 0 END) AS Null_Tenure,
SUM(CASE WHEN Satisfaction IS NULL THEN 1 ELSE 0 END) AS Null_Satisfaction,
SUM(CASE WHEN Bonus IS NULL THEN 1 ELSE 0 END) AS Null_Bonus,
SUM(CASE WHEN Avg_Hrs_Month IS NULL THEN 1 ELSE 0 END) AS Null_Avg_Hrs_Month,
SUM(CASE WHEN [Left] IS NULL THEN 1 ELSE 0 END) AS Null_Left
FROM
PortfolioProject.dbo.employee_churn_data

-- Average satisfaction by department
SELECT 
Department, 
AVG(Satisfaction) AS Avg_Satisfaction
FROM 
PortfolioProject.dbo.employee_churn_data
GROUP BY 
Department
ORDER BY 
Avg_Satisfaction DESC

-- Departments with the highest average tenure
SELECT 
Department, 
AVG(Tenure) AS Avg_Tenure
FROM 
PortfolioProject.dbo.employee_churn_data
GROUP BY 
Department
ORDER BY 
Avg_Tenure DESC

-- Employees with high performance and low satisfaction
SELECT 
*
FROM 
PortfolioProject.dbo.employee_churn_data
WHERE 
Review > 0.75 
AND Satisfaction < 0.5

-- Percentage of employees who left by salary level
SELECT 
Salary, 
COUNT(CASE WHEN [Left] = 'Yes' THEN 1 END) * 100.0 / COUNT(*) AS Left_Percentage
FROM 
PortfolioProject.dbo.employee_churn_data
GROUP BY 
Salary
ORDER BY 
Left_Percentage DESC

-- Number of employees in each department who received a bonus

SELECT 
Department, 
COUNT(*) AS Num_Bonuses
FROM 
PortfolioProject.dbo.employee_churn_data
WHERE 
Bonus = 1
GROUP BY 
Department
ORDER BY 
Num_Bonuses DESC
