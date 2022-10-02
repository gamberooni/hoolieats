with rename_cols as (
    select
        userID as user_id,
        placeID as place_id,
        rating as overall_rating,
        * exclude (userID, placeID, rating)
    from {{ ref('rating_final') }}
)

select
    *
from rename_cols
left join {{ ref('users_denorm') }} using (user_id)
left join {{ ref('restaurants_denorm') }} using (place_id)
