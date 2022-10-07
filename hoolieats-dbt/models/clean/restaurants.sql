with base as (
    select
        * exclude (operating_days),
        case operating_days
            when 'Mon;Tue;Wed;Thu;Fri' then 'Weekdays'
            else operating_days
        end as operating_days,
        str_split(operating_hours, '-')[1] as opening_hours,
        str_split(operating_hours, '-')[2] as closing_hours,
    from {{ ref('restaurants_denorm') }}
),

avg_ratings as (
    select
        place_id,
        round(avg(overall_rating), 2) AS avg_rating,
        round(avg(food_rating), 2) AS avg_food_rating,
        round(avg(service_rating), 2) AS avg_service_rating,
        count(user_id) AS rating_count
    from {{ ref('ratings') }}
    inner join {{ ref('users') }} using (user_id)
    group by place_id
)

select
    *,
    PERCENT_RANK() OVER (
        ORDER BY avg_rating DESC, avg_food_rating DESC, avg_service_rating DESC, rating_count DESC
    ) AS pcrnk
from base
inner join avg_ratings using (place_id)
