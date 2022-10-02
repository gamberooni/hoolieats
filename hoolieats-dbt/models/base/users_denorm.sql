with users_joined as (
    select
        *
    from {{ ref('userprofile') }}
    left join {{ ref('userpayment') }} using (userID)
    left join {{ ref('usercuisine') }} using (userID)
)

select
    userID as user_id,
    Rcuisine as cuisine,
    Upayment as payment,
    latitude as user_latitude,
    longitude as user_longitude,
    * exclude (userID, Rcuisine, Upayment, latitude, longitude)
from users_joined
