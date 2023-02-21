SELECT 
*
FROM
PortfolioProject.dbo.CovidDeaths
WHERE
continent is not NULL
ORDER BY
3,4


--SELECT
--*
--FROM
--PortfolioProject.dbo.CovidVaccinations
--ORDER BY
--3,4

--SELECT THE DATA THAT WILL BE USED


SELECT
location,
date,
total_cases,
new_cases,
total_deaths,
population
FROM
PortfolioProject.dbo.CovidDeaths
WHERE
continent is not NULL
ORDER BY
1,2

-- LOOKING AT TOTAL CASES VS TOTAL DEATHS
--SHOWS LIKELIHOOD OF DYING FROM CONTRACTING COVID IN YOUR COUNTRY
SELECT
location,
date,
total_cases,
total_deaths,
(CONVERT(float, total_deaths) / CONVERT(float, total_cases))*100 AS Death_percentage
FROM
PortfolioProject.dbo.CovidDeaths
WHERE
location = 'South Africa' AND 
continent is not NULL
ORDER BY
1,2


-- LOOKING AT TOTAL CASES VS POPULATION
-- SHOWS PERCENTAGE OF POPULATION THAT CONTRACTED COVID
SELECT
location,
date,
total_cases,
population,
(CONVERT(float, total_cases) / CONVERT(float, population))*100 AS Case_percentage
FROM
PortfolioProject.dbo.CovidDeaths
--WHERE
--location = 'South Africa'
WHERE
continent is not NULL
ORDER BY
1,2

--LOOKING AT COUNTRIES WITH THE HIGHEST COVID CONTRACTION RATE COMPARED TO POPULATION


SELECT
location,
population,
MAX(total_cases)  AS highest_contraction_rate,
MAX (CONVERT(float, total_cases) / CONVERT(float, population))*100 AS Case_percentage
FROM
PortfolioProject.dbo.CovidDeaths
--WHERE
--location = 'South Africa'
WHERE
continent is not NULL
GROUP BY
location,
population
ORDER BY
Case_percentage DESC

--LOOKING AT COUNTRIES WITH THE HIGHEST COVID DEATH RATE PER POPULATION


SELECT
location,
MAX (CAST(CAST(total_deaths AS FLOAT) AS INT))  AS highest_death_rate
FROM
PortfolioProject.dbo.CovidDeaths
WHERE
continent is not NULL
GROUP BY
location
ORDER BY
highest_death_rate DESC

-- BREAK THINGS DOWN BY CONTINENT

-- SHOWING CONTINENTS WITH HIGHEST DEATH RATE
SELECT
continent,
MAX (CAST(CAST(total_deaths AS FLOAT) AS INT))  AS highest_death_rate
FROM
PortfolioProject.dbo.CovidDeaths
WHERE
continent is not NULL
GROUP BY
continent
ORDER BY
highest_death_rate DESC


--SHOWING CONTINENTS WITH HIGHEST CONTRACTION RATE

SELECT
continent,
MAX (CAST(CAST(total_cases AS FLOAT) AS INT))  AS highest_contraction_rate
FROM
PortfolioProject.dbo.CovidDeaths
WHERE
continent is not NULL
GROUP BY
continent
ORDER BY
highest_contraction_rate DESC


--GLOBAL NUMBERS FOR CASES

SELECT
date,
SUM(CONVERT(INT, CONVERT(FLOAT, new_cases))) AS total_new_cases
FROM
PortfolioProject.dbo.CovidDeaths
WHERE
continent is not NULL
GROUP BY
date
ORDER BY
1,2

--GLOBAL NUMBERS FOR DEATHS
SELECT
date,
SUM(CONVERT(INT, CONVERT(FLOAT, new_deaths))) AS total_new_deaths
FROM
PortfolioProject.dbo.CovidDeaths
WHERE
continent is not NULL
GROUP BY
date
ORDER BY
1,2

-- LOOKING AT TOTAL VACCINATIONS VS TOTAL POPULATION 


SELECT
dea.continent,
dea.location,
dea.date,
dea.population,
vac.new_vaccinations
FROM
PortfolioProject.dbo.CovidDeaths dea
JOIN
PortfolioProject.dbo.CovidVaccinations vac
ON
dea.date = vac.date
AND dea.location = vac.location
WHERE
dea.continent is not NULL 
AND vac.new_vaccinations is not NULL
ORDER BY
2,3



--CREATING VIEW TO STORE DATA FOR VISUALISATION LATER

CREATE VIEW covid_stats AS
SELECT
dea.continent,
dea.location,
dea.date,
dea.population,
vac.new_vaccinations
FROM
PortfolioProject.dbo.CovidDeaths dea
JOIN
PortfolioProject.dbo.CovidVaccinations vac
ON
dea.date = vac.date
AND dea.location = vac.location
WHERE
dea.continent is not NULL 
AND vac.new_vaccinations is not NULL