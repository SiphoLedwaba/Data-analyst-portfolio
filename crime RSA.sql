-- Checking contents of SouthAfricaCrimeStats
SELECT 
*
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats

-- Checking contents of ProvincePopulation
SELECT 
*
FROM 
PortfolioProject.dbo.ProvincePopulation

-- Checking for null values in critical columns
SELECT 
COUNT(*) AS Null_Values,
COUNT(Province) AS Non_Null_Province,
COUNT(Category) AS Non_Null_Category
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
WHERE 
Province IS NULL OR Category IS NULL

-- Total crimes by province and category
SELECT 
Province,
Category,
SUM([2005-2006] + 
[2006-2007] + 
[2007-2008] + 
[2008-2009] + 
[2009-2010] + 
[2010-2011] + 
[2011-2012] + 
[2012-2013] + 
[2013-2014] + 
[2014-2015] + 
[2015-2016]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Province, 
Category
ORDER BY
Total_Crimes DESC

-- Total crimes by province
SELECT 
Province,
SUM([2005-2006] + 
[2006-2007] + 
[2007-2008] + 
[2008-2009] + 
[2009-2010] + 
[2010-2011] + 
[2011-2012] + 
[2012-2013] + 
[2013-2014] + 
[2014-2015] + 
[2015-2016]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Province
ORDER BY 
Total_Crimes DESC

-- Total crimes by year
SELECT 
'2005-2006' AS Year, SUM([2005-2006]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2006-2007' AS Year, SUM([2006-2007]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2007-2008' AS Year, SUM([2007-2008]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2008-2009' AS Year, SUM([2008-2009]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2009-2010' AS Year, SUM([2009-2010]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2010-2011' AS Year, SUM([2010-2011]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2011-2012' AS Year, SUM([2011-2012]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2012-2013' AS Year, SUM([2012-2013]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2013-2014' AS Year, SUM([2013-2014]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2014-2015' AS Year, SUM([2014-2015]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
UNION ALL
SELECT 
'2015-2016' AS Year, SUM([2015-2016]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
ORDER BY 
Year

-- Average population density by province
SELECT 
Province,
AVG(Density) AS Avg_Density
FROM 
PortfolioProject.dbo.ProvincePopulation
GROUP BY
Province

-- Joining Crime Stats with Population Data and calculating Crime Rate per 100k people
SELECT 
A.Province,
A.Category,
SUM(
A.[2005-2006] + 
A.[2006-2007] + 
A.[2007-2008] + 
A.[2008-2009] + 
A.[2009-2010] + 
A.[2010-2011] + 
A.[2011-2012] + 
A.[2012-2013] + 
A.[2013-2014] + 
A.[2014-2015] + 
A.[2015-2016]) AS Total_Crimes,
B.Population,
(SUM(
A.[2005-2006] + 
A.[2006-2007] + 
A.[2007-2008] + 
A.[2008-2009] + 
A.[2009-2010] + 
A.[2010-2011] + 
A.[2011-2012] + 
A.[2012-2013] + 
A.[2013-2014] + 
A.[2014-2015] + 
A.[2015-2016]) / B.Population) * 100000 AS Crime_Rate_Per_100k
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats A
JOIN 
PortfolioProject.dbo.ProvincePopulation B ON A.Province = B.Province
GROUP BY 
A.Province, 
A.Category, 
B.Population
ORDER BY 
Crime_Rate_Per_100k DESC

-- Crime Trends per Year by Province and Category
SELECT 
Province,
Category,
SUM([2005-2006]) AS Crimes_2005_2006,
SUM([2006-2007]) AS Crimes_2006_2007,
SUM([2007-2008]) AS Crimes_2007_2008,
SUM([2008-2009]) AS Crimes_2008_2009,
SUM([2009-2010]) AS Crimes_2009_2010,
SUM([2010-2011]) AS Crimes_2010_2011,
SUM([2011-2012]) AS Crimes_2011_2012,
SUM([2012-2013]) AS Crimes_2012_2013,
SUM([2013-2014]) AS Crimes_2013_2014,
SUM([2014-2015]) AS Crimes_2014_2015,
SUM([2015-2016]) AS Crimes_2015_2016
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Province, 
Category
ORDER BY 
Province, 
Category

-- Total crimes by station
SELECT 
Station,
SUM([2005-2006] + 
[2006-2007] + 
[2007-2008] + 
[2008-2009] + 
[2009-2010] + 
[2010-2011] + 
[2011-2012] + 
[2012-2013] + 
[2013-2014] + 
[2014-2015] + 
[2015-2016]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
ORDER BY 
Total_Crimes DESC

-- Average crime rate per station per year
WITH Crime_Stats AS (
SELECT 
Station,
'2005-2006' AS Year, 
SUM([2005-2006]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2006-2007' AS Year,
SUM([2006-2007]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2007-2008' AS Year, 
SUM([2007-2008]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2008-2009' AS Year,
SUM([2008-2009]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2009-2010' AS Year,
SUM([2009-2010]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2010-2011' AS Year,
SUM([2010-2011]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2011-2012' AS Year,
SUM([2011-2012]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2012-2013' AS Year,
SUM([2012-2013]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2013-2014' AS Year,
SUM([2013-2014]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2014-2015' AS Year,
SUM([2014-2015]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
UNION ALL
SELECT 
Station,
'2015-2016' AS Year,
SUM([2015-2016]) AS Total_Crimes
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats
GROUP BY 
Station
)
SELECT 
Station,
AVG(Total_Crimes) AS Avg_Crime_Rate
FROM 
Crime_Stats
GROUP BY 
Station
ORDER BY 
Avg_Crime_Rate DESC

-- Crime rate per 100k people per station
SELECT 
A.Station,
SUM(A.[2005-2006] + 
A.[2006-2007] + 
A.[2007-2008] + 
A.[2008-2009] + 
A.[2009-2010] + 
A.[2010-2011] + 
A.[2011-2012] + 
A.[2012-2013] + 
A.[2013-2014] + 
A.[2014-2015] + 
A.[2015-2016]) AS Total_Crimes,
B.Population,
(SUM(A.[2005-2006] + 
A.[2006-2007] + 
A.[2007-2008] + 
A.[2008-2009] + 
A.[2009-2010] + 
A.[2010-2011] + 
A.[2011-2012] + 
A.[2012-2013] + 
A.[2013-2014] + 
A.[2014-2015] + 
A.[2015-2016]) / NULLIF(B.Population, 0)) * 100000 AS Crime_Rate_Per_100k
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats A
JOIN 
PortfolioProject.dbo.ProvincePopulation B ON A.Province = B.Province
GROUP BY 
A.Station, 
B.Population
ORDER BY 
Crime_Rate_Per_100k DESC

-- Average crime rate per province per 100k people
SELECT 
A.Province,
B.Population,
SUM(
A.[2005-2006] + 
A.[2006-2007] + 
A.[2007-2008] + 
A.[2008-2009] + 
A.[2009-2010] + 
A.[2010-2011] + 
A.[2011-2012] + 
A.[2012-2013] + 
A.[2013-2014] + 
A.[2014-2015] + 
A.[2015-2016]
) / 11.0 AS Avg_Crimes_Per_Year,
(SUM(
A.[2005-2006] + 
A.[2006-2007] + 
A.[2007-2008] + 
A.[2008-2009] + 
A.[2009-2010] + 
A.[2010-2011] + 
A.[2011-2012] + 
A.[2012-2013] + 
A.[2013-2014] + 
A.[2014-2015] + 
A.[2015-2016]
) / 11.0) / NULLIF(B.Population, 0) * 100000 AS Avg_Crime_Rate_Per_100k 
FROM 
PortfolioProject.dbo.SouthAfricaCrimeStats A
JOIN 
PortfolioProject.dbo.ProvincePopulation B ON A.Province = B.Province
GROUP BY 
A.Province, 
B.Population
ORDER BY 
Avg_Crime_Rate_Per_100k DESC
