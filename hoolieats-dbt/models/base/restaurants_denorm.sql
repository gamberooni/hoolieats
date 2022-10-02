with restaurants_joined as (
    select
        *
    from {{ ref('geoplaces2') }}
    left join {{ ref('chefmozaccepts') }} using (placeID)
    left join {{ ref('chefmozcuisine') }} using (placeID)
    left join {{ ref('chefmozhours4') }} using (placeID)
    left join {{ ref('chefmozparking') }} using (placeID)
)

select
    placeID as place_id,
    * exclude (placeID, Rpayment, Rcuisine, hours, days),
    Rpayment as payment_method,
    Rcuisine as cuisine,
    hours as operating_hours,
    days as operating_days
from restaurants_joined
