with restaurants_joined as (
    select
        *
    from {{ ref('geoplaces2') }}
    left join {{ ref('chefmozaccepts') }} using (placeID)
    left join {{ ref('chefmozcuisine') }} using (placeID)
    left join {{ ref('chefmozhours4') }} using (placeID)
    left join {{ ref('chefmozparking') }} using (placeID)
),

string_cleaning as (
    select
        * exclude (days, hours),
        case
            when Rpayment = 'Visa' then 'VISA'
            else Rpayment
        end as Rpayment,
        rtrim(days, ';') as days,
        rtrim(hours, ';') as hours
    from restaurants_joined
)

select
    placeID as place_id,
    Rpayment as payment_method,
    Rcuisine as cuisine,
    Rambience as ambience,
    hours as operating_hours,
    days as operating_days,
    latitude as place_latitude,
    longitude as place_longitude,
    * exclude (placeID, Rpayment, Rcuisine, Rambience, hours, days, latitude, longitude)
from string_cleaning
