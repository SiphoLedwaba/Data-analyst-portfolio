--Bringing out the dataset
SELECT
*
FROM
PortfolioProject.dbo.fashion_product

--Top products based on average rating
SELECT TOP 10
[pid] AS product_id, 
title, 
brand, 
category, 
sub_category, 
(CAST(REPLACE(selling_price, ',', '') AS DECIMAL(10, 2))) AS selling_price, 
(CAST(average_rating AS DECIMAL(3, 2))) AS average_rating, 
discount 
FROM 
PortfolioProject.dbo.fashion_product
ORDER BY 
average_rating DESC, 
CAST(REPLACE(discount, '% off', '') AS DECIMAL(5, 2)) DESC 

--Brands with the highest rating
SELECT TOP 5
brand,  
(CAST(average_rating AS DECIMAL(3, 2))) AS average_rating
FROM 
PortfolioProject.dbo.fashion_product
WHERE
brand is not null
ORDER BY 
average_rating DESC 


--Products from the same brand with the highest rating

SELECT TOP 5
title, 
(CAST(REPLACE(selling_price, ',', '') AS DECIMAL(10, 2))) AS selling_price, 
(CAST(average_rating AS DECIMAL(3, 2))) AS average_rating
FROM 
PortfolioProject.dbo.fashion_product
WHERE 
brand = 'Jagdish Garmen' 
group by
title, 
selling_price, 
average_rating
ORDER BY 
average_rating DESC 


--Products that are out of stock
SELECT 
COUNT(*) AS out_of_stock_count
FROM 
PortfolioProject.dbo.fashion_product
WHERE 
out_of_stock = 1

--Product details and pricing comparison
SELECT 
[pid] AS product_id, 
title, 
actual_price, 
CAST(REPLACE(selling_price, ',', '') AS DECIMAL(10, 2)) AS selling_price, 
CAST(REPLACE(actual_price, ',', '') AS DECIMAL(10, 2)) - CAST(REPLACE(selling_price, ',', '') AS DECIMAL(10, 2)) AS discount_amount, 
description, 
product_details 
FROM 
PortfolioProject.dbo.fashion_product 
WHERE 
category = 'Clothing and Accessories' 
AND sub_category = 'Bottomwear'

--Products with high discounts
SELECT 
[pid] AS product_id, 
title, 
brand, 
category, 
sub_category, 
selling_price, 
discount 
FROM 
PortfolioProject.dbo.fashion_product
WHERE 
CAST(REPLACE(discount, '% off', '') AS DECIMAL(5, 2)) >= 50 
ORDER BY 
discount DESC

--Products within each sub-category based on their average rating and price
SELECT 
[pid] AS product_id, 
title, 
brand, 
category, 
sub_category, 
selling_price, 
(CAST(average_rating AS DECIMAL(3, 2))) AS average_rating, 
RANK() OVER (PARTITION BY sub_category ORDER BY average_rating DESC, selling_price ASC) AS sub_category_rank
FROM 
PortfolioProject.dbo.fashion_product
ORDER BY 
sub_category_rank

--Average selling price and rating for each brand
SELECT 
brand, 
AVG(CAST(REPLACE(selling_price, ',', '') AS DECIMAL(10, 2))) AS average_selling_price, 
AVG(CAST(average_rating AS DECIMAL(3, 2))) AS average_rating, 
COUNT(pid) AS number_of_products
FROM 
PortfolioProject.dbo.fashion_product
GROUP BY 
brand
ORDER BY 
average_rating DESC,
average_selling_price ASC

--Products with an above-average rating in each category
SELECT 
fp.pid AS product_id, 
fp.title, 
fp.brand, 
fp.category, 
fp.sub_category, 
fp.selling_price, 
fp.average_rating
FROM 
PortfolioProject.dbo.fashion_product fp
WHERE 
fp.average_rating > (
SELECT 
AVG(CAST(fp_inner.average_rating AS DECIMAL(3, 2)))
FROM 
PortfolioProject.dbo.fashion_product fp_inner
WHERE 
fp_inner.category = fp.category
)
ORDER BY 
fp.average_rating DESC

--Categorising products into pricing tiers
SELECT 
[pid] AS product_id, 
title, 
brand, 
category, 
sub_category, 
CAST(REPLACE(selling_price, ',', '') AS DECIMAL(10, 2)) AS selling_price, 
CASE 
WHEN CAST(REPLACE(selling_price, ',', '') AS DECIMAL(10, 2)) < 500 THEN 'Budget'
WHEN CAST(REPLACE(selling_price, ',', '') AS DECIMAL(10, 2)) BETWEEN 500 AND 1000 THEN 'Mid-range'
ELSE 'Premium'
END AS price_tier
FROM 
PortfolioProject.dbo.fashion_product
ORDER BY 
price_tier,
selling_price ASC

--Searching for products with keywords in the description
SELECT 
[pid] AS product_id, 
title, 
brand, 
description
FROM 
PortfolioProject.dbo.fashion_product
WHERE 
description LIKE '%cotton%' 
OR description LIKE '%comfortable%'
ORDER BY 
average_rating DESC

--Products where certain fields have null values and replace with a default value
SELECT 
[pid] AS product_id, 
title, 
brand, 
COALESCE(CAST(REPLACE(selling_price, ',', '') AS DECIMAL(10, 2)), 0) AS selling_price,  
COALESCE(CAST(average_rating AS DECIMAL(3, 2)), 0) AS average_rating 
FROM 
PortfolioProject.dbo.fashion_product
WHERE 
selling_price IS NULL OR average_rating IS NULL
