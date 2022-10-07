# read payment methods table, do array_agg to wrap all payment methods as an array,
# 	then join with geoplaces2 table
# same with cuisines, hours and parking tables
# also read ratings table, calculate average ratings and rating count for each restaurant,
# 	then join with geoplaces2 table
# additionally, do a percent_rank() calculation based on, in order, average rating,
# 	avg food rating, avg service rating and rating count
restaurant_view = """
SELECT
	avg_rating,
	avg_food_rating,
	avg_service_rating,
	rating_count,
	payment_methods,
	parking_lot,
	cuisines,
	business_hours,
	g."placeID",
	latitude,
	longitude,
	g.name,
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
	other_services,
	PERCENT_RANK() OVER (
			ORDER BY avg_rating DESC, avg_food_rating DESC, avg_service_rating DESC, rating_count DESC
		) AS pcrnk
FROM geoplaces2 AS g
LEFT JOIN
	(SELECT
		name,
		rating_final."placeID",
		ROUND(avg(rating), 2) AS avg_rating,
		ROUND(avg(food_rating), 2) AS avg_food_rating,
		ROUND(avg(service_rating), 2) AS avg_service_rating,
		COUNT("userID") AS rating_count
		FROM rating_final
	JOIN geoplaces2
	ON geoplaces2."placeID" = rating_final."placeID"
	GROUP BY name, rating_final."placeID"
	ORDER BY avg_rating DESC, avg_food_rating DESC, avg_service_rating DESC, rating_count DESC
	) AS r
ON r."placeID" = g."placeID"
LEFT JOIN
	(SELECT "placeID", ARRAY_AGG(chefmozaccepts."Rpayment") as payment_methods
	FROM chefmozaccepts
	GROUP BY "placeID"
	) AS ca
ON ca."placeID" = g."placeID"
LEFT JOIN
	(SELECT "placeID", ARRAY_AGG(chefmozcuisine."Rcuisine") AS cuisines
	FROM chefmozcuisine
	GROUP BY "placeID"
	) AS cc
ON cc."placeID" = g."placeID"
LEFT JOIN
	(SELECT "placeID", ARRAY_AGG(chefmozparking.parking_lot) AS parking_lot
	FROM chefmozparking
	GROUP BY "placeID"
	) AS cp
ON cp."placeID" = g."placeID"
LEFT JOIN
	(SELECT "placeID", ARRAY_AGG(ARRAY[days, hours]) AS business_hours
	FROM chefmozhours4
	GROUP BY "placeID"
	) AS ch
ON ch."placeID" = g."placeID";
"""

customer_view = """
SELECT
	bmi,
	u."userID",
	latitude,
	longitude,
	smoker,
	drink_level,
	dress_preference,
	ambience,
	transport,
	marital_status,
	hijos,
	birth_year,
	interest,
	personality,
	religion,
	activity,
	color,
	weight,
	budget,
	height,
	(2011-birth_year) AS age,
	CASE
		WHEN bmi < 18.5 THEN 'underweight'
		WHEN bmi >= 18.5 AND bmi < 25 THEN 'normal'
		WHEN bmi >= 25 AND bmi < 30 THEN 'overweight'
		WHEN bmi > 30 THEN 'obese'
		ELSE 'N/A'
	END bmi_status
FROM userprofile AS u
LEFT JOIN
	(SELECT
	 	"userID",
		ROUND(CAST((weight/pow(height,2)) AS numeric), 2) AS bmi
	FROM userprofile
	) AS b
ON b."userID" = u."userID";
"""

rating_behavior_view = """
SELECT
	r.rating,
	r.food_rating,
	r.service_rating,
	r."userID",
	r."placeID",
	accessibility AS raccessibility,
	area AS rarea,
	other_services AS rother_services,
	url AS rurl,
	franchise AS rfranchise,
	cc.cuisines AS rcuisines,
	uc.cuisines AS ucuisines,
	cp.parking_lot AS rparking,
	u.transport AS utransport,
	smoking_area AS rsmoking_area,
	smoker AS csmoker,
	dress_code AS rdress_code,
	dress_preference AS cdress_preference,
	price AS rprice,
	budget AS ubudget,
	alcohol AS ralcohol,
	drink_level AS udrink_level,
	rpayment.payment_methods AS rpayment,
	upayment.payment_methods AS upayment,
	CASE
		WHEN transport = 'car owner' THEN 'true'
		WHEN transport = 'N/A' THEN 'N/A'
		ELSE 'false'
	END AS uneeds_parking_lot,
	CASE
		WHEN g.smoking_area = 'section' THEN 'true'
		WHEN g.smoking_area = 'only at bar' THEN 'true'
		WHEN g.smoking_area = 'permitted' THEN 'true'
		WHEN g.smoking_area = 'none' THEN 'false'
		WHEN g.smoking_area = 'not permitted' THEN 'false'
		ELSE 'N/A'
	END AS rsmoking_allowed,
	CASE
		WHEN g.url != 'N/A' and g.url != 'no' THEN 'true'
		ELSE 'false'
	END AS rhas_url,
	CASE
		WHEN g.price = u.budget THEN 'true'
		WHEN g.price = 'N/A' OR u.budget = 'N/A' THEN 'N/A'
		else 'false'
	END AS price_budget_matched
FROM rating_final as r
LEFT JOIN
	(SELECT "placeID", ARRAY_AGG(chefmozaccepts."Rpayment") AS payment_methods
	FROM chefmozaccepts
	GROUP BY "placeID"
	) AS rpayment
ON rpayment."placeID" = r."placeID"
LEFT JOIN
	(SELECT "userID", ARRAY_AGG(userpayment."Upayment") AS payment_methods
	FROM userpayment
	GROUP BY "userID") AS upayment
ON upayment."userID" = r."userID"
LEFT JOIN
	(SELECT "placeID", ARRAY_AGG(chefmozcuisine."Rcuisine") AS cuisines
	FROM chefmozcuisine
	GROUP BY "placeID"
	) AS cc
ON cc."placeID" = r."placeID"
LEFT JOIN
	(SELECT "userID", ARRAY_AGG(usercuisine."Rcuisine") AS cuisines
	FROM usercuisine
	GROUP BY "userID"
	) AS uc
ON uc."userID" = r."userID"
LEFT JOIN
	(SELECT "placeID", ARRAY_AGG(chefmozparking.parking_lot) AS parking_lot
	FROM chefmozparking
	GROUP BY "placeID"
	) AS cp
ON r."placeID" = cp."placeID"
LEFT JOIN userprofile AS u
ON u."userID" = r."userID"
LEFT JOIN geoplaces2 AS g
ON g."placeID" = r."placeID";
"""

rhas_parking_lot = """
CREATE OR REPLACE VIEW rbview
AS
SELECT
	*,
	CASE
		WHEN 'none'=ANY(rparking) THEN 'false'
		ELSE 'true'
	END AS rhas_parking_lot
FROM rbview_tmp;
"""
