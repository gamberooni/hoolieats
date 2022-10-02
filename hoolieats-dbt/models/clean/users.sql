with base as (
    select
        *,
        round(cast((weight/pow(height,2)) AS numeric), 2) AS bmi
    from {{ ref('users_denorm') }}
)

select
    *,
    (2011-birth_year) AS age,
	case
		when bmi < 18.5 then 'underweight'
		when bmi >= 18.5 and bmi < 25 then 'normal'
		when bmi >= 25 and bmi < 30 then 'overweight'
		when bmi > 30 then 'obese'
		else 'N/A'
	end bmi_status
from base
