SELECT
*
FROM
PortfolioProject.dbo.DailyMerged

---- Droping TrackerDistance column
--ALTER TABLE PortfolioProject.dbo.DailyMerged
--DROP COLUMN TrackerDistance;

--calculating total steps per day

SELECT 
ActivityDay,
Sum(TotalSteps) as TotalSteps
from
PortfolioProject.dbo.DailyMerged
group by
activityday

-- calculating total distance per day

SELECT 
ActivityDay,
Sum(TotalDistance) as TotalDistance
from
PortfolioProject.dbo.DailyMerged
group by
activityday

-- calculating average steps taken per day
SELECT 
ActivityDay,
avg(TotalSteps) as AverageSteps
from
PortfolioProject.dbo.DailyMerged
group by
activityday

-- calculating average distance per day
SELECT 
ActivityDay,
avg(TotalDistance) as AverageDistance
from
PortfolioProject.dbo.DailyMerged
group by
activityday

-- identifying top 10 users with highest total steps
SELECT TOP 10 Id,
SUM(TotalSteps) AS TotalSteps
FROM
PortfolioProject.dbo.DailyMerged
GROUP BY 
Id
ORDER BY 
TotalSteps DESC;

-- calculating the total distance covered per user
SELECT Id, 
SUM(TotalDistance) AS TotalDistance
FROM 
PortfolioProject.dbo.DailyMerged
GROUP BY 
Id;

-- analysing the distribution of activity minutes
SELECT
SUM(VeryActiveMinutes_x) AS TotalVeryActiveMinutes,
SUM(FairlyActiveMinutes_x) AS TotalFairlyActiveMinutes,
SUM(LightlyActiveMinutes_x) AS TotalLightlyActiveMinutes,
SUM(SedentaryMinutes_x) AS TotalSedentaryMinutes
FROM
PortfolioProject.dbo.DailyMerged;

--  analyzing activity level trends over time
SELECT 
ActivityDay,
SUM(VeryActiveMinutes_x) AS TotalVeryActiveMinutes,
SUM(FairlyActiveMinutes_x) AS TotalFairlyActiveMinutes,
SUM(LightlyActiveMinutes_x) AS TotalLightlyActiveMinutes,
SUM(SedentaryMinutes_x) AS TotalSedentaryMinutes
FROM 
PortfolioProject.dbo.DailyMerged
GROUP BY 
ActivityDay
ORDER BY 
ActivityDay;

-- identifying users with consistently high activity levels
WITH UserActivity AS (
    SELECT 
        Id,
        AVG(VeryActiveMinutes_x) AS AvgVeryActiveMinutes,
        AVG(FairlyActiveMinutes_x) AS AvgFairlyActiveMinutes,
        AVG(LightlyActiveMinutes_x) AS AvgLightlyActiveMinutes,
        AVG(SedentaryMinutes_x) AS AvgSedentaryMinutes
    FROM 
        PortfolioProject.dbo.DailyMerged
    GROUP BY 
        Id
)
SELECT 
Id,
AVG(AvgVeryActiveMinutes) AS AvgVeryActiveMinutes,
AVG(AvgFairlyActiveMinutes) AS AvgFairlyActiveMinutes,
AVG(AvgLightlyActiveMinutes) AS AvgLightlyActiveMinutes,
AVG(AvgSedentaryMinutes) AS AvgSedentaryMinutes
FROM 
UserActivity
GROUP BY 
Id
ORDER BY 
AVG(AvgVeryActiveMinutes) DESC;

-- analyzing trends in calories burned per day
SELECT 
ActivityDay,
SUM(Calories_x) AS TotalCaloriesBurned
FROM 
PortfolioProject.dbo.DailyMerged
GROUP BY 
ActivityDay
ORDER BY 
    ActivityDay;

-- investigating the relationship between activity level and total steps
SELECT 
 SUM(TotalSteps) AS TotalSteps,
 SUM(VeryActiveMinutes_x) AS TotalVeryActiveMinutes,
 SUM(FairlyActiveMinutes_x) AS TotalFairlyActiveMinutes,
 SUM(LightlyActiveMinutes_x) AS TotalLightlyActiveMinutes,
 SUM(SedentaryMinutes_x) AS TotalSedentaryMinutes
FROM 
PortfolioProject.dbo.DailyMerged;

-- analyzing the distribution of activity distances
SELECT 
SUM(VeryActiveDistance_x) AS TotalVeryActiveDistance,
SUM(ModeratelyActiveDistance_x) AS TotalModeratelyActiveDistance,
SUM(LightActiveDistance_x) AS TotalLightActiveDistance,
SUM(SedentaryActiveDistance_x) AS TotalSedentaryActiveDistance
FROM 
PortfolioProject.dbo.DailyMerged;

-- identifying days with the highest and lowest activity levels
SELECT 
ActivityDay,
SUM(VeryActiveMinutes_x + FairlyActiveMinutes_x + LightlyActiveMinutes_x + SedentaryMinutes_x) AS TotalActiveMinutes
FROM 
PortfolioProject.dbo.DailyMerged
GROUP BY 
ActivityDay
ORDER BY 
TotalActiveMinutes DESC
OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY; -- Highest activity day

SELECT 
ActivityDay,
SUM(VeryActiveMinutes_x + FairlyActiveMinutes_x + LightlyActiveMinutes_x + SedentaryMinutes_x) AS TotalActiveMinutes
FROM 
PortfolioProject.dbo.DailyMerged
GROUP BY 
ActivityDay
ORDER BY 
TotalActiveMinutes 
OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY; -- Lowest activity day

-- calculating the average activity level per user
SELECT 
Id,
AVG(VeryActiveMinutes_x + FairlyActiveMinutes_x + LightlyActiveMinutes_x + SedentaryMinutes_x) AS AvgTotalActiveMinutes
FROM 
PortfolioProject.dbo.DailyMerged
GROUP BY 
Id
ORDER BY 
AvgTotalActiveMinutes DESC;

-- investigating the relationship between activity level and total calories burned
SELECT 
SUM(Calories_x) AS TotalCaloriesBurned,
SUM(VeryActiveMinutes_x + FairlyActiveMinutes_x + LightlyActiveMinutes_x + SedentaryMinutes_x) AS TotalActiveMinutes
FROM 
PortfolioProject.dbo.DailyMerged;

-- analyzing sedentary behavior patterns throughout the week
SELECT 
DATEPART(WEEKDAY, ActivityDay) AS DayOfWeek,
AVG(SedentaryMinutes_x) AS AvgSedentaryMinutes
FROM 
PortfolioProject.dbo.DailyMerged
GROUP BY 
DATEPART(WEEKDAY, ActivityDay)
ORDER BY 
DayOfWeek;
