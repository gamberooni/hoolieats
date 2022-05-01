# customers
customer_available_payment_methods = """
SELECT
	COUNT(*),
	"Upayment"
FROM userpayment
GROUP BY "Upayment"
ORDER BY count DESC;
"""

customer_preferred_cuisines = """
SELECT
	COUNT(*),
	"Rcuisine"
FROM usercuisine
GROUP BY "Rcuisine"
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;
"""

customer_marital_status = """
SELECT
	marital_status,
	COUNT(*) FROM userprofile
GROUP BY marital_status;
"""

customer_is_smoker = """
SELECT
	smoker,
	COUNT(*) FROM userprofile
GROUP BY smoker;
"""

customer_drink_level = """
SELECT
	drink_level,
	COUNT(*) FROM userprofile
GROUP BY drink_level;
"""

customer_dress_preference = """
SELECT
	dress_preference,
	COUNT(*) FROM userprofile
GROUP BY dress_preference;
"""

customer_ambience = """
SELECT
	ambience,
	COUNT(*) FROM userprofile
GROUP BY ambience;
"""

customer_transport = """
SELECT
	transport,
	COUNT(*) FROM userprofile
GROUP BY transport;
"""

customer_hijos = """
SELECT
	hijos,
	COUNT(*) FROM userprofile
GROUP BY hijos;
"""

customer_personality = """
SELECT
	personality,
	COUNT(*) FROM userprofile
GROUP BY personality;
"""

customer_activity = """
SELECT
	activity,
	COUNT(*) FROM userprofile
GROUP BY activity;
"""

customer_budget = """
SELECT
	budget,
	COUNT(*) FROM userprofile
GROUP BY budget;
"""

customer_age = """
SELECT
	age
FROM cview;
"""

customer_bmi_status = """
SELECT
	COUNT(*),
	bmi_status
FROM cview
GROUP BY bmi_status
ORDER BY array_position(array['N/A','underweight','normal','overweight','obese'], cview.bmi_status);
"""

customer_religion = """
SELECT
	religion,
	COUNT(*) FROM userprofile
GROUP BY religion;
"""

customer_color = """
SELECT
	color,
	COUNT(*) FROM userprofile
GROUP BY color;
"""

customer_profile = """
SELECT
	count(*),
	bmi_status,
	marital_status,
	smoker,
	drink_level,
	ambience,
	personality,
	budget
FROM cview
GROUP BY
	bmi_status,
	marital_status,
	smoker,
	drink_level,
	ambience,
	personality,
	budget
HAVING count(*) > 1
ORDER BY count DESC;
"""
