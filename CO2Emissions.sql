SELECT
*
fROM
PortfolioProject.dbo.CO2_emission

--SHOWING DATA WE WILL BE USING

SELECT
country,
year,
CO2_emissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
WHERE
CO2_emissions_metric_tonne > '0' 
ORDER BY
1,2

--CALCULATING TOTAL EMISSIONS
SELECT
SUM (CAST(CO2_emissions_metric_tonne AS FLOAT))  AS TotalEmissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission

--CALCULATING THE TOTAL CARBON DIOXIDE EMISSIONS BY COUNTRY
SELECT
country,
SUM (CAST(CO2_emissions_metric_tonne AS FLOAT))  AS TotalEmissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY
country
ORDER BY
country

--CALCULATING THE TOTAL CARBON DIOXIDE EMISSIONS BY REGION
SELECT
region,
SUM (CAST(CO2_emissions_metric_tonne AS FLOAT))  AS totalEmissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY
region
ORDER BY
region 

--CALCULATING THE TOTAL CARBON DIOXIDE EMISSIONS BY YEAR

SELECT
year,
SUM(Cast(CO2_emissions_metric_tonne as float)) AS totalEmissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
year
ORDER BY
year

--CALCULATING THE TOTAL CARBON DIOXIDE EMISSIONS BY REGION AND YEAR

SELECT
Region,
year,
SUM (CAST(CO2_emissions_metric_tonne as float)) AS totalCO2Emissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
Region,
year
ORDER BY
totalCO2Emissions_metric_tonne DESC

--CALCULATING THE AVERAGE CARBON DIOXIDE EMISSIONS BY COUNTRY

SELECT
country,
AVG (CAST(CO2_emissions_metric_tonne AS FLOAT))  AS AvgEmissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY
country
ORDER BY
country

--CALCULATING THE AVERAGE CARBON DIOXIDE EMISSIONS BY REGION

SELECT
Region,
AVG(Cast(CO2_emissions_metric_tonne as float)) AS AvgEmissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
Region
ORDER BY
Region

--CALCULATING THE AVERAGE CARBON DIOXIDE EMISSIONS BY YEAR

SELECT
year,
AVG(Cast(CO2_emissions_metric_tonne as float)) AS AvgEmissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
year
ORDER BY
year


--CALCULATING THE HIGHEST CARBON DIOXIDE EMISSIONS BY COUNTRY

SELECT
country,
MAX (CAST (CO2_emissions_metric_tonne as float)) AS highest_CO2Emissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
country
ORDER BY
highest_CO2Emissions_metric_tonne  DESC

--CALCULATING THE HIGHEST CARBON DIOXIDE EMISSIONS BY REGION

SELECT
Region,
MAX (CAST(CO2_emissions_metric_tonne as float)) AS highest_CO2Emissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY
Region
ORDER BY
highest_CO2Emissions_metric_tonne DESC

--CALCULATING THE HIGHEST CARBON DIOXIDE EMISSIONS BY REGION AND YEAR
SELECT
Region,
year,
MAX (CAST(CO2_emissions_metric_tonne as float)) AS highest_CO2Emissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
Region,
year
ORDER BY
highest_CO2Emissions_metric_tonne DESC

--CALCULATING THE LOWEST CARBON DIOXIDE EMISSIONS BY REGION AND YEAR
SELECT
Region,
year,
MAX (CAST(CO2_emissions_metric_tonne as float)) AS lowest_CO2Emissions_metric_tonne
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
Region,
year
ORDER BY
lowest_CO2Emissions_metric_tonne

