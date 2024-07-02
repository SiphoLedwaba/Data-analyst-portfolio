-- Whole dataset
select
* 
From
PortfolioProject.dbo.healthcare_dataset

-- Average age by gender
SELECT 
AVG(Age) as avg_age,
Gender
FROM
PortfolioProject.dbo.healthcare_dataset
GROUP BY
Gender

-- Total count by blood type
SELECT
[Blood Type],
COUNT(*) as Total
FROM
PortfolioProject.dbo.healthcare_dataset
GROUP BY
[Blood Type]
ORDER BY
[Blood Type]

-- Total billing amount by insurance provider
SELECT 
[Insurance Provider],
SUM([Billing Amount]) as Total_Billing
FROM
PortfolioProject.dbo.healthcare_dataset
GROUP BY
[Insurance Provider]
ORDER BY
Total_Billing DESC

-- Number of patients admitted each month
SELECT
FORMAT([Date of Admission], 'yyyy-MM') as Admission_Month,
COUNT(*) as Patient_Count
FROM
PortfolioProject.dbo.healthcare_dataset
GROUP BY
FORMAT([Date of Admission], 'yyyy-MM')
ORDER BY
Admission_Month

-- Average billing amount by admission type
SELECT
[Admission Type],
AVG([Billing Amount]) as Avg_Billing
FROM
PortfolioProject.dbo.healthcare_dataset
GROUP BY
[Admission Type]
ORDER BY
Avg_Billing DESC

-- Count of patients by medical condition
SELECT
[Medical Condition],
COUNT(*) as Patient_Count
FROM
PortfolioProject.dbo.healthcare_dataset
GROUP BY
[Medical Condition]
ORDER BY
Patient_Count DESC

-- Count of patients by doctor
SELECT
Doctor,
COUNT(*) as Patient_Count
FROM
PortfolioProject.dbo.healthcare_dataset
GROUP BY
Doctor
ORDER BY
Patient_Count DESC

-- Average length of stay by hospital (assuming discharge date is not null)
SELECT 
Hospital,
AVG(DATEDIFF(day, [Date of Admission], [Discharge Date])) as Avg_Length_of_Stay
FROM
PortfolioProject.dbo.healthcare_dataset
WHERE
[Discharge Date] IS NOT NULL
GROUP BY
Hospital
ORDER BY
Avg_Length_of_Stay DESC

-- Count of patients by room number
SELECT
[Room Number],
COUNT(*) as Patient_Count
FROM
PortfolioProject.dbo.healthcare_dataset
GROUP BY
[Room Number]
ORDER BY
Patient_Count DESC

