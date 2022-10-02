select
    *,
    {{ dbt_utils.surrogate_key(['user_id', 'place_id']) }} as upsert_key
from {{ ref('ratings_base') }}
