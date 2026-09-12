WITH base AS (
	SELECT *
	FROM product_emissions
	WHERE year = (
		SELECT MAX(year)
		FROM product_emissions
	)
)

SELECT
	industry_group,
	COUNT (DISTINCT company) AS num_companies,
	ROUND(SUM(carbon_footprint_pcf), 1) AS total_industry_footprint
FROM base
GROUP BY industry_group
ORDER BY total_industry_footprint DESC;