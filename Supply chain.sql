-- loading dataset

select
*
from
portfolioproject.dbo.supply_chain_data

-- number of items per product type

SELECT
product_type,
COUNT(*) as  Nunmber_of_products
FROM
portfolioproject.dbo.supply_chain_data
GROUP BY
product_type


-- number of items per supplier

SELECT
Supplier_name,
COUNT(*) as  Nunmber_of_products
FROM
portfolioproject.dbo.supply_chain_data
GROUP BY
Supplier_name

--total revenue
SELECT 
SUM(Revenue_Generated) AS TotalRevenue
FROM 
portfolioproject.dbo.supply_chain_data

--average price per product type
SELECT 
Product_Type, 
AVG(Price) AS AveragePrice
FROM 
portfolioproject.dbo.supply_chain_data
GROUP BY 
Product_Type

--total number of products sold
SELECT 
Product_Type, 
SUM(Number_Of_Products_Sold) AS TotalProductsSold
FROM 
portfolioproject.dbo.supply_chain_data
GROUP BY 
Product_Type

--total number of products sold per supplier
SELECT 
supplier_name, 
SUM(Number_Of_Products_Sold) AS TotalProductsSold
FROM 
portfolioproject.dbo.supply_chain_data
GROUP BY 
Supplier_name

-- top 5 products by revenue
SELECT top 5
SKU,
Revenue_Generated
FROM 
PortfolioProject.dbo.supply_chain_data
ORDER BY
Revenue_Generated DESC

-- stock levels and lead times analysis
SELECT 
Product_Type, 
AVG(Stock_Levels) AS Average_Stock_Level,
AVG(Lead_Times) AS Average_Lead_Time
FROM 
PortfolioProject.dbo.supply_chain_data
GROUP BY
Product_Type

--shipping costs by carrier
SELECT 
Shipping_Carriers, 
SUM(Shipping_Costs) AS Total_Shipping_Cost
FROM 
PortfolioProject.dbo.supply_chain_data
GROUP BY 
Shipping_Carriers

-- revenue by customer demographics
SELECT 
Customer_Demographics, 
SUM(Revenue_Generated) AS Total_Revenue
FROM 
PortfolioProject.dbo.supply_chain_data
GROUP BY 
Customer_Demographics

-- average defect rate by product type
SELECT 
Product_Type,
AVG(Defect_Rates) AS Average_Defect_Rate
FROM 
PortfolioProject.dbo.supply_chain_data
GROUP BY
Product_Type

-- average defect rate by supplier type
SELECT
Supplier_name,
AVG(Defect_Rates) AS Average_Defect_Rate
FROM 
PortfolioProject.dbo.supply_chain_data
GROUP BY
Supplier_name

-- pass/fail inspection results
SELECT 
Inspection_Results,
COUNT(*) AS Count
FROM 
PortfolioProject.dbo.supply_chain_data
GROUP BY 
Inspection_Results

-- product performance quick access

CREATE VIEW
product_performance AS(
SELECT 
SKU,
Product_Type,
SUM(Number_Of_Products_Sold) AS TotalSold,
SUM(Revenue_Generated) AS TotalRevenue
FROM
PortfolioProject.dbo.supply_chain_data
GROUP BY 
SKU, 
Product_Type)



-- shipping analysis quick access

CREATE VIEW 
shipping_analysis AS(
SELECT
Shipping_Carriers,
SUM(Shipping_Costs) AS TotalShippingCost,
AVG(Shipping_Times) AS AverageShippingTime
FROM 
PortfolioProject.dbo.supply_chain_data
GROUP BY 
Shipping_Carriers)
