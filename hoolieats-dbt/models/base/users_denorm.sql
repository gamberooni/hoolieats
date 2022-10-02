with users_joined as (
    select
        *
    from {{ ref('userprofile') }}
    left join {{ ref('userpayment') }} using (userID)
    left join {{ ref('usercuisine') }} using (userID)
)

select
    userID as user_id,
    * exclude (userID, Rcuisine, Upayment),
    Rcuisine as cuisine,
    Upayment as payment
from users_joined
