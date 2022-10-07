# rating behavior
rating_count = """
SELECT
  count(*),
  rating
FROM rbview
GROUP BY rating
ORDER BY array_position(array[0, 1, 2], rbview.rating::integer);
"""

food_rating_count = """
SELECT
  count(*),
  food_rating
FROM rbview
GROUP BY food_rating
ORDER BY array_position(array[0, 1, 2], rbview.food_rating::integer);
"""

service_rating_count = """
SELECT
  count(*),
  service_rating
FROM rbview
GROUP BY service_rating
ORDER BY array_position(array[0, 1, 2], rbview.service_rating::integer);
"""

payment_methods = """
SELECT
	rpayment @> upayment AS offered,
	v.*,
	count(*)
FROM rbview AS rb,
LATERAL(
	VALUES
		('rating', rb.rating),
		('food', rb.food_rating),
		('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rpayment @> upayment, v.rating_type, v.rating_value
ORDER BY v.rating_type, v.rating_value, offered;
"""

cuisines = """
SELECT
	rcuisines @> ucuisines AS offered,
	v.*,
	count(*)
FROM rbview AS rb,
LATERAL(
	VALUES
		('rating', rb.rating),
		('food', rb.food_rating),
		('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rcuisines @> ucuisines, v.rating_type, v.rating_value
ORDER BY v.rating_type, v.rating_value, offered;
"""

rarea = """
SELECT count(*), rb.rarea, v.*
FROM rbview AS rb,
LATERAL(
	VALUES
		('rating', rb.rating),
		('food', rb.food_rating),
		('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rb.rarea, v.rating_type, v.rating_value
ORDER BY v.rating_type, v.rating_value, rb.rarea DESC;
"""

raccessibility = """
SELECT COUNT(*), rb.raccessibility, v.*
FROM rbview AS rb,
LATERAL(
	VALUES
		('rating', rb.rating),
		('food', rb.food_rating),
		('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rb.raccessibility, v.rating_type, v.rating_value
ORDER BY v.rating_type, v.rating_value;
"""

rother_services = """
SELECT COUNT(*), rb.rother_services, v.*
FROM rbview AS rb,
LATERAL(
	VALUES
		('rating', rb.rating),
		('food', rb.food_rating),
		('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rb.rother_services, v.rating_type, v.rating_value
ORDER BY v.rating_type, v.rating_value;
"""

rfranchise = """
SELECT COUNT(*), rb.rfranchise, v.*
FROM rbview AS rb,
LATERAL(
	VALUES
		('rating', rb.rating),
		('food', rb.food_rating),
		('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rb.rfranchise, v.rating_type, v.rating_value
ORDER BY v.rating_type, v.rating_value, rb.rfranchise;
"""

smoking_allowed = """
SELECT COUNT(*), rb.rsmoking_allowed, v.*
FROM rbview AS rb,
LATERAL(
    VALUES
        ('rating', rb.rating),
        ('food', rb.food_rating),
        ('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rb.rsmoking_allowed, v.rating_type, v.rating_value
ORDER BY v.rating_type, v.rating_value, rb.rsmoking_allowed;
"""

price_budget_matched = """
SELECT COUNT(*), rb.price_budget_matched, v.*
FROM rbview AS rb,
LATERAL(
    VALUES
        ('rating', rb.rating),
        ('food', rb.food_rating),
        ('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rb.price_budget_matched, v.rating_type, v.rating_value
ORDER BY
    v.rating_type,
    v.rating_value,
    array_position(array['N/A', 'false', 'true'],
    rb.price_budget_matched
);
"""

ralcohol = """
SELECT COUNT(*), rb.ralcohol, v.*
FROM rbview AS rb,
LATERAL(
	VALUES
		('rating', rb.rating),
		('food', rb.food_rating),
		('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rb.ralcohol, v.rating_type, v.rating_value
ORDER BY
	v.rating_type,
	v.rating_value,
	array_position(array['No_Alcohol_Served', 'Wine-Beer', 'Full_Bar'], rb.ralcohol);
"""

rhas_url = """
SELECT COUNT(*), rb.rhas_url, v.*
FROM rbview AS rb,
LATERAL(
	VALUES
		('rating', rb.rating),
		('food', rb.food_rating),
		('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY rb.rhas_url, v.rating_type, v.rating_value
ORDER BY v.rating_type, v.rating_value, rb.rhas_url;
"""

parking_needs_fulfilled = """
SELECT
	CASE
		when uneeds_parking_lot=rhas_parking_lot then 'false'
		else 'true'
	END AS fulfilled,
	v.*,
	COUNT(*)
FROM rbview AS rb,
LATERAL(
	VALUES
		('rating', rb.rating),
		('food', rb.food_rating),
		('service', rb.service_rating)
) AS v (rating_type, rating_value)
GROUP BY fulfilled, v.rating_type, v.rating_value
ORDER BY v.rating_type, v.rating_value, fulfilled;
"""

# crosstab_example =
# '''
# SELECT has_url
#      , COALESCE(rating_0, 0) AS "rating_0"
#      , COALESCE(rating_1, 0) AS "rating_1"
#      , COALESCE(rating_2, 0) AS "rating_2"
# FROM crosstab(
#        'SELECT
# 			case
# 				when rurl != ''N/A'' and rurl != ''no'' then ''true''
# 				else ''false''
# 			end as has_url,
# 			rating,
# 			count(*)
# 		FROM rbview
# 		GROUP BY has_url, rating
# 		ORDER BY 1'

#        ,$$VALUES (0), (1), (2)$$
#  ) AS ct (
#    has_url text
#  , rating_0 int
#  , rating_1 int
#  , rating_2 int);
# '''
