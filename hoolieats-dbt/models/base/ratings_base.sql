select
    userID as user_id,
    placeID as place_id,
    rating as overall_rating,
    * exclude (userID, placeID, rating)
from {{ ref('rating_final') }}
