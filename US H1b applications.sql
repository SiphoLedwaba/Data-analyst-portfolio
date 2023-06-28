-- Retrieving all columns from datasets
SELECT 
*
FROM
PortfolioProject.dbo.[h-1b_data2021]
UNION ALL
SELECT 
*
FROM
PortfolioProject.dbo.[h-1b_data2022]
UNION ALL
SELECT 
*
FROM
PortfolioProject.dbo.[h-1b_data2023]

--Counting the total number of records in each dataset

SELECT 
COUNT(*) AS record_number,
'2021' AS fiscal_year
FROM
PortfolioProject.dbo.[h-1b_data2021]
UNION ALL
SELECT 
COUNT(*) AS record_number,
'2022' AS fiscal_year
FROM
PortfolioProject.dbo.[h-1b_data2022]
UNION ALL
SELECT 
COUNT(*) AS record_number,
'2023' AS fiscal_year
FROM
PortfolioProject.dbo.[h-1b_data2023]

--Calculating the average approval and denial rates for each fiscal year
SELECT 
    [Fiscal Year],
    AVG([Initial Approval]) AS avg_initial_approval_rate,
    AVG([Initial Denial]) AS avg_initial_denial_rate,
    AVG([Continuing Approval]) AS avg_continuing_approval_rate,
    AVG([Continuing Denial]) AS avg_continuing_denial_rate
FROM 
PortfolioProject.dbo.[h-1b_data2021]
GROUP BY 
[Fiscal Year]
UNION ALL
SELECT 
    [Fiscal Year],
    AVG([Initial Approval]) AS avg_initial_approval_rate,
    AVG([Initial Denial]) AS avg_initial_denial_rate,
    AVG([Continuing Approval]) AS avg_continuing_approval_rate,
    AVG([Continuing Denial]) AS avg_continuing_denial_rate
FROM 
PortfolioProject.dbo.[h-1b_data2022]
GROUP BY 
[Fiscal Year]
UNION ALL
SELECT 
    [Fiscal Year],
    AVG([Initial Approval]) AS avg_initial_approval_rate,
    AVG([Initial Denial]) AS avg_initial_denial_rate,
    AVG([Continuing Approval]) AS avg_continuing_approval_rate,
    AVG([Continuing Denial]) AS avg_continuing_denial_rate
FROM 
PortfolioProject.dbo.[h-1b_data2023]
GROUP BY 
[Fiscal Year]


SELECT 
AVG([Initial Approval] )
FROM
PortfolioProject.dbo.[h-1b_data2021]

--Finding the top 10 employers with the highest number of initial approvals in each fiscal year
SELECT
TOP 10
Employer,
[Initial Approval],
[Fiscal Year]
FROM
PortfolioProject.dbo.[h-1b_data2021]
UNION ALL
SELECT
TOP 10
Employer,
[Initial Approval],
[Fiscal Year]
FROM
PortfolioProject.dbo.[h-1b_data2022]
WHERE
Employer is not NULL
UNION ALL
SELECT
TOP 10
Employer,
[Initial Approval],
[Fiscal Year]
FROM
PortfolioProject.dbo.[h-1b_data2023]
ORDER BY
[Initial Approval] DESC

--Calculating the total number of approvals and denials by NAICS code in each fiscal year
SELECT
SUM([Initial Approval] + [Continuing Approval]) AS total_approval,
SUM([Initial Denial]+ [Continuing Denial]) AS total_denial,
[Fiscal Year],
NAICS
FROM
PortfolioProject.dbo.[h-1b_data2021]
GROUP BY
[Fiscal Year],
NAICS
UNION ALL
SELECT
SUM([Initial Approval] + [Continuing Approval]) AS total_approval,
SUM([Initial Denial]+ [Continuing Denial]) AS total_denial,
[Fiscal Year],
NAICS
FROM
PortfolioProject.dbo.[h-1b_data2022]
GROUP BY
[Fiscal Year],
NAICS
UNION ALL
SELECT
SUM([Initial Approval] + [Continuing Approval]) AS total_approval,
SUM([Initial Denial]+ [Continuing Denial]) AS total_denial,
[Fiscal Year],
NAICS
FROM
PortfolioProject.dbo.[h-1b_data2023]
GROUP BY
[Fiscal Year],
NAICS

--Finding the top 10 states with the highest number of H1B approvals
SELECT
TOP 10
[Fiscal Year],
State,
COUNT(*) as approval_number
FROM
PortfolioProject.dbo.[h-1b_data2021]
WHERE
State is not NULL AND
([Initial Approval] ='1' OR [Continuing Approval] ='1')
GROUP BY
[Fiscal Year],
State
UNION ALL
SELECT
TOP 10
[Fiscal Year],
State,
COUNT(*) as approval_number
FROM
PortfolioProject.dbo.[h-1b_data2022]
WHERE
State is not NULL AND
([Initial Approval] ='1' OR [Continuing Approval] ='1')
GROUP BY
[Fiscal Year],
State
UNION ALL
SELECT
TOP 10
[Fiscal Year],
State,
COUNT(*) as approval_number
FROM
PortfolioProject.dbo.[h-1b_data2023]
WHERE
State is not NULL AND ([Initial Approval] ='1' OR [Continuing Approval] ='1')
GROUP BY
[Fiscal Year],
State
ORDER BY
approval_number DESC

--Finding the top 10 cities with the highest number of H1B approvals
SELECT
TOP 10
[Fiscal Year],
City,
COUNT(*) as approval_number
FROM
PortfolioProject.dbo.[h-1b_data2021]
WHERE
City is not NULL AND
([Initial Approval] ='1' OR [Continuing Approval] ='1')
GROUP BY
[Fiscal Year],
City
UNION ALL
SELECT
TOP 10
[Fiscal Year],
CIty,
COUNT(*) as approval_number
FROM
PortfolioProject.dbo.[h-1b_data2022]
WHERE
City is not NULL AND 
([Initial Approval] ='1' OR [Continuing Approval] ='1')
GROUP BY
[Fiscal Year],
City
UNION ALL
SELECT
TOP 10
[Fiscal Year],
CIty,
COUNT(*) as approval_number
FROM
PortfolioProject.dbo.[h-1b_data2023]
WHERE
City is not NULL AND
([Initial Approval] ='1' OR [Continuing Approval] ='1')
GROUP BY
[Fiscal Year],
City
ORDER BY
approval_number DESC

--Calculate the approval rate for each state in each fiscal year
SELECT
[Fiscal Year],
State,
COUNT(*) AS total_approvals,
SUM([Initial Approval] + [Continuing Approval]) AS total_records,
CAST((COUNT(*) * 100.0 / SUM([Initial Approval] + [Continuing Approval])) AS DECIMAL(10,2)) AS approval_rate
FROM
PortfolioProject.dbo.[h-1b_data2021]
WHERE
State IS NOT NULL
GROUP BY
[Fiscal Year],
State
UNION ALL
SELECT
[Fiscal Year],
State,
COUNT(*) AS total_approvals,
SUM([Initial Approval] + [Continuing Approval]) AS total_records,
CAST((COUNT(*) * 100.0 / SUM([Initial Approval] + [Continuing Approval])) AS DECIMAL(10,2)) AS approval_rate
FROM
PortfolioProject.dbo.[h-1b_data2022]
WHERE
State IS NOT NULL
GROUP BY
[Fiscal Year],
State
UNION ALL
SELECT
[Fiscal Year],
State,
COUNT(*) AS total_approvals,
SUM([Initial Approval] + [Continuing Approval]) AS total_records,
CAST((COUNT(*) * 100.0 / SUM([Initial Approval] + [Continuing Approval])) AS DECIMAL(10,2)) AS approval_rate
FROM
PortfolioProject.dbo.[h-1b_data2023]
WHERE
State IS NOT NULL
GROUP BY
[Fiscal Year],
State
ORDER BY
approval_rate DESC


--Calculate the approval rate for each city in  each fiscal year

SELECT
[Fiscal Year],
City,
COUNT(*) AS total_approvals,
SUM([Initial Approval] + [Continuing Approval]) AS total_records,
CASE
WHEN SUM([Initial Approval] + [Continuing Approval]) = 0 THEN 0
ELSE (COUNT(*) * 100.0 / SUM([Initial Approval] + [Continuing Approval]))
END AS approval_rate
FROM
PortfolioProject.dbo.[h-1b_data2021]
WHERE
City IS NOT NULL
GROUP BY
[Fiscal Year],
City
UNION ALL
SELECT
[Fiscal Year],
City,
COUNT(*) AS total_approvals,
SUM([Initial Approval] + [Continuing Approval]) AS total_records,
CASE
WHEN SUM([Initial Approval] + [Continuing Approval]) = 0 THEN 0
ELSE (COUNT(*) * 100.0 / SUM([Initial Approval] + [Continuing Approval]))
END AS approval_rate
FROM
PortfolioProject.dbo.[h-1b_data2022]
WHERE
City IS NOT NULL
GROUP BY
[Fiscal Year],
City
UNION ALL
SELECT
[Fiscal Year],
City,
COUNT(*) AS total_approvals,
SUM([Initial Approval] + [Continuing Approval]) AS total_records,
CASE
WHEN SUM([Initial Approval] + [Continuing Approval]) = 0 THEN 0
ELSE (COUNT(*) * 100.0 / SUM([Initial Approval] + [Continuing Approval]))
END AS approval_rate
FROM
PortfolioProject.dbo.[h-1b_data2023]
WHERE
City IS NOT NULL
GROUP BY
[Fiscal Year],
City
ORDER BY
approval_rate DESC