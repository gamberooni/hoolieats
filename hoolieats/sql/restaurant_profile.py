# restaurants
top_five_best_restaurant = """
SELECT
	name,
	avg_rating,
	avg_food_rating,
	avg_service_rating,
	rating_count
FROM restaurants
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
FROM restaurants
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
FROM restaurants
WHERE pcrnk >= ? AND pcrnk <= ?
ORDER BY random()
LIMIT 5;
"""

restaurant_profile = """
SELECT
    payment_method,
    parking_lot,
    cuisine,
    operating_hours,
    opening_hours,
    closing_hours,
    place_id,
    place_latitude,
    place_longitude,
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
    ambience,
    franchise,
    area,
    other_services
FROM restaurants
WHERE name = ?;
"""

rcuisines = """
SELECT
    COUNT(*) as count,
    cuisine
FROM restaurants
GROUP BY cuisine
HAVING COUNT(*) > 6
ORDER BY COUNT(*) DESC;
"""

rpayment_methods = """
SELECT
    COUNT(*) as count,
    payment_method
FROM restaurants
GROUP BY payment_method
ORDER BY COUNT(*) DESC;
"""
