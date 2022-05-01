# restaurants
top_five_best_restaurant = """
SELECT
	name,
	avg_rating,
	avg_food_rating,
	avg_service_rating,
	rating_count
FROM rview
ORDER BY pcrnk
LIMIT 5;
"""

top_five_worst_restaurant = """
SELECT
	name,
	avg_rating,
	avg_food_rating,
	avg_service_rating,
	rating_count
FROM rview
ORDER BY pcrnk DESC
LIMIT 5;
"""

random_five_restaurant_within_percentile = """
SELECT
	name,
	avg_rating,
	avg_food_rating,
	avg_service_rating,
	rating_count
FROM rview
WHERE pcrnk >= %s AND pcrnk <= %s
ORDER BY random()
LIMIT 5;
"""

restaurant_profile = """
SELECT
	payment_methods,
	parking_lot,
	cuisines,
	business_hours,
	"placeID",
	latitude,
	longitude,
	name,
	address,
	city,
	state,
	country,
	fax,
	zip,
	alcohol,
	smoking_area,
	dress_code,
	accessibility,
	price,
	url,
	"Rambience",
	franchise,
	area,
	other_services
FROM rview
WHERE name = %s;
"""

rcuisines = """
SELECT
	COUNT(*),
	"Rcuisine"
FROM chefmozcuisine
GROUP BY "Rcuisine"
HAVING COUNT(*) > 6
ORDER BY COUNT(*) DESC;
"""

rpayment_methods = """
SELECT
	COUNT(*),
	"Rpayment"
FROM chefmozaccepts
GROUP BY "Rpayment"
ORDER BY COUNT(*) DESC;
"""
