-- Load Dataset
SELECT
    *
FROM
    PortfolioProject.dbo.Superstore_Sales_Cleaned;

-- Calculate total revenue
SELECT 
    SUM(CAST(REPLACE(REPLACE([Sales], ',', ''), '$', '') AS DECIMAL(18, 2))) as TotalRevenue
FROM 
    PortfolioProject.dbo.Superstore_Sales_Cleaned;

-- Calculate average order value
SELECT 
    AVG(CAST(REPLACE(REPLACE([Sales], ',', ''), '$', '') AS DECIMAL(18, 2))) as AvgOrderValue
FROM 
    PortfolioProject.dbo.Superstore_Sales_Cleaned;

-- Calculate total customers and orders
SELECT 
    COUNT(DISTINCT [Customer Name]) as TotalCustomers,
    COUNT([Order Date]) as TotalOrders
FROM 
    PortfolioProject.dbo.Superstore_Sales_Cleaned;

-- Calculate average revenue per customer
SELECT 
    SUM(CAST(REPLACE(REPLACE([Sales], ',', ''), '$', '') AS DECIMAL(18, 2))) / COUNT(DISTINCT [Customer Name]) as AvgRevenuePerCustomer 
FROM
    PortfolioProject.dbo.Superstore_Sales_Cleaned;

-- Identify top-selling products
SELECT 
    TOP 10
    [Sub-Category],
    SUM(CAST(REPLACE(REPLACE([Sales], ',', ''), '$', '') AS DECIMAL(18, 2))) as TotalSales
FROM
    PortfolioProject.dbo.Superstore_Sales_Cleaned
GROUP BY 
    [Sub-Category]
ORDER BY 
    TotalSales DESC;

-- Analyze sales by region
SELECT
    [Region],
    SUM(CAST(REPLACE(REPLACE([Sales], ',', ''), '$', '') AS DECIMAL(18, 2))) as TotalSalesByRegion
FROM 
    PortfolioProject.dbo.Superstore_Sales_Cleaned
GROUP BY 
    [Region]
ORDER BY 
    TotalSalesByRegion DESC;

-- Calculate conversion rate
SELECT 
    COUNT(DISTINCT [Order Date]) as TotalOrders,
    COUNT(DISTINCT [Customer Name]) as TotalCustomers,
    (COUNT(DISTINCT [Order Date]) * 100.0 / COUNT(DISTINCT [Customer Name])) as ConversionRate
FROM 
    PortfolioProject.dbo.Superstore_Sales_Cleaned;

-- Identify high-value customers (top 10 by total spending)
SELECT TOP 10
    [Customer Name],
    SUM(CAST(REPLACE(REPLACE([Sales], ',', ''), '$', '') AS DECIMAL(18, 2))) as TotalSpending
FROM 
    PortfolioProject.dbo.Superstore_Sales_Cleaned
GROUP BY 
    [Customer Name]
ORDER BY
    TotalSpending DESC;

-- Monthly Sales Trend
SELECT 
    DATEPART(year, [Order Date]) as OrderYear,
    DATEPART(month, [Order Date]) as OrderMonth,
    SUM(CAST(REPLACE(REPLACE([Sales], ',', ''), '$', '') AS DECIMAL(18, 2))) as MonthlySales
FROM 
    PortfolioProject.dbo.Superstore_Sales_Cleaned
GROUP BY 
    DATEPART(year, [Order Date]), DATEPART(month, [Order Date])
ORDER BY 
    OrderYear, OrderMonth;

-- Profit Margin
SELECT 
    [Sub-Category], 
    AVG(CAST(REPLACE(REPLACE([Sales - Boost], ',', ''), '$', '') AS DECIMAL(18, 2))) as AverageProfit
FROM 
    PortfolioProject.dbo.Superstore_Sales_Cleaned
GROUP BY 
    [Sub-Category];

-- Sales Distribution by Ship Mode
SELECT 
    [Ship Mode],
    SUM(CAST(REPLACE(REPLACE([Sales], ',', ''), '$', '') AS DECIMAL(18, 2))) as TotalSales
FROM 
    PortfolioProject.dbo.Superstore_Sales_Cleaned
GROUP BY 
    [Ship Mode];
