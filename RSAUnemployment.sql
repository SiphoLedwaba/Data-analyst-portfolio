--TOTAL NUMBER OF UNEMPLOYED PEOPLE IN SOUTH AFRICA
SELECT
COUNT (*) AS totalunemployed
FROM
PortfolioProject.dbo.RSADOEUnemployment

--CALCULATING TOTAL NUMBER OF UNEMPLOYED MALES VS FEMALES

SELECT 
COUNT(*) AS totalmales
FROM
PortfolioProject.dbo.RSADOEUnemployment
WHERE
gender = 'Male'

SELECT
COUNT(*) AS totalfemales
FROM
PortfolioProject.dbo.RSADOEUnemployment
WHERE 
gender = 'Female'


--CALCULATING RATE OF UNEMPLOYEMENT BY GENDER
SELECT 
Gender,
COUNT(*) as total_unemployed, 
ROUND(CAST(COUNT(*) as FLOAT) / (SELECT COUNT(*) FROM PortfolioProject.dbo.RSADOEUnemployment WHERE Gender is not NULL ) * 100, 2) as unemployment_rate
FROM
PortfolioProject.dbo.RSADOEUnemployment
WHERE 
Gender is not NULL
GROUP BY
Gender

--CALCULATING RATE OF UNEMPLOYEMENT BY RACE

SELECT
Race,
COUNT(*) as total_unemployed, 
ROUND(CAST(COUNT(*) as FLOAT) / (SELECT COUNT(*) FROM PortfolioProject.dbo.RSADOEUnemployment WHERE Race is not NULL) * 100, 2) as unemployment_rate
FROM PortfolioProject.dbo.RSADOEUnemployment
WHERE 
Race is not NULL
GROUP BY 
Race

--CALCULATING PROVINCES WITH THE HIGHEST TOTAL UNEMPLOYMENT
SELECT
Province,
COUNT(*) as total_unemployed
FROM
PortfolioProject.dbo.RSADOEUnemployment
WHERE
Province is not NULL
GROUP BY
Province 


--CALCULATING PROVINCES WITH THE HIGHEST UNEMPLOYMENT RATE
SELECT
Province,
COUNT(*) as total_unemployed, 
ROUND(CAST(COUNT(*) as FLOAT) / (SELECT COUNT(*) FROM PortfolioProject.dbo.RSADOEUnemployment WHERE Province is not NULL) * 100, 2) as unemployment_rate
FROM PortfolioProject.dbo.RSADOEUnemployment
WHERE
Province is not NULL
GROUP BY
Province 

--CALCULATING TOTAL EXPERIENCE OF THE UNEMPLOYED

SELECT
OverallExperience,
COUNT(*) as total_employed
FROM 
PortfolioProject.dbo.RSADOEUnemployment
WHERE
OverallExperience is not NULL
GROUP BY 
OverallExperience
