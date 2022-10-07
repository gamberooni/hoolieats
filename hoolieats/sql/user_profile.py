# users
user_available_payment_methods = """
SELECT
    COUNT(*) as count,
    payment
FROM users
GROUP BY payment
ORDER BY count DESC;
"""

user_preferred_cuisines = """
SELECT
    COUNT(*) as count,
    cuisine
FROM users
GROUP BY cuisine
HAVING COUNT(*)
ORDER BY count DESC;
"""

user_marital_status = """
SELECT
    marital_status,
    COUNT(*) as count
FROM users
GROUP BY marital_status;
"""

user_is_smoker = """
SELECT
	smoker,
	COUNT(*) as count
FROM users
GROUP BY smoker;
"""

user_drink_level = """
SELECT
	drink_level,
	COUNT(*) as count
FROM users
GROUP BY drink_level;
"""

user_dress_preference = """
SELECT
	dress_preference,
	COUNT(*) as count
FROM users
GROUP BY dress_preference;
"""

user_ambience = """
SELECT
	ambience,
	COUNT(*) as count
FROM users
GROUP BY ambience;
"""

user_transport = """
SELECT
	transport,
	COUNT(*) as count
FROM users
GROUP BY transport;
"""

user_hijos = """
SELECT
	hijos,
	COUNT(*) as count
FROM users
GROUP BY hijos;
"""

user_personality = """
SELECT
    personality,
    COUNT(*) as count
FROM users
GROUP BY personality;
"""

user_activity = """
SELECT
    activity,
    COUNT(*) as count
FROM users
GROUP BY activity;
"""

user_budget = """
SELECT
    budget,
    COUNT(*) as count
FROM users
GROUP BY budget;
"""

user_bmi_status = """
SELECT
    COUNT(*) as count,
    bmi_status
FROM users
GROUP BY bmi_status
ORDER BY array_position(array['N/A','underweight','normal','overweight','obese'], users.bmi_status);
"""

user_religion = """
SELECT
    religion,
    COUNT(*) as count
FROM users
GROUP BY religion;
"""

user_color = """
SELECT
    color,
    COUNT(*) as count
FROM users
GROUP BY color;
"""

user_profile = """
SELECT
    COUNT(*) as count,
    bmi_status,
    marital_status,
    smoker,
    drink_level,
    ambience,
    personality,
    budget
FROM users
GROUP BY
    bmi_status,
    marital_status,
    smoker,
    drink_level,
    ambience,
    personality,
    budget
-- HAVING COUNT(*)
ORDER BY count DESC;
"""
