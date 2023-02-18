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

--CALCULATING THE TOTAL CARBON DIOXIDE EMISSIONS BY COUNTRY
SELECT
country,
SUM (CAST(CO2_emissions_metric_tonne AS FLOAT))  AS TotalEmissions
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY
country
ORDER BY
country

--CALCULATING THE TOTAL CARBON DIOXIDE EMISSIONS BY REGION
SELECT
region,
SUM (CAST(CO2_emissions_metric_tonne AS FLOAT))  AS totalEmissions
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY
region
ORDER BY
region

--CALCULATING THE AVERAGE CARBON DIOXIDE EMISSIONS BY COUNTRY

SELECT
country,
AVG (CAST(CO2_emissions_metric_tonne AS FLOAT))  AS AvgEmissions
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY
country
ORDER BY
country

--CALCULATING THE AVERAGE CARBON DIOXIDE EMISSIONS BY REGION

SELECT
Region,
year,
AVG(Cast(CO2_emissions_metric_tonne as float)) AS AvgEmissions
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
Region,
year
ORDER BY
Region,
year

--CALCULATING THE HIGHEST CARBON DIOXIDE EMISSIONS BY COUNTRY

SELECT
country,
MAX (CAST (CO2_emissions_metric_tonne as float)) AS highest_CO2Emissions
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
country
ORDER BY
highest_CO2Emissions DESC

--CALCULATING THE AVERAGE CARBON DIOXIDE EMISSIONS BY REGION

SELECT
Region,
MAX (CAST(CO2_emissions_metric_tonne as float)) AS highest_CO2Emissions
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
Region
ORDER BY
highest_CO2Emissions DESC

--CALCULATING THE HIGHEST CARBON DIOXIDE EMISSIONS YEAR BY REGION AND COUNTRY
SELECT
country,
Region,
year,
MAX (CAST(CO2_emissions_metric_tonne as float)) AS highest_CO2Emissions
FROM
PortfolioProject.dbo.CO2_emission
GROUP BY 
country,
Region,
year
ORDER BY
highest_CO2Emissions DESC

