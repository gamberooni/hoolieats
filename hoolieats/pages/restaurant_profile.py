import pydeck as pdk
import streamlit as st
from utils.plot_utils import *

import hoolieats.sql as sql
from hoolieats import query_executor


def app():
    st.title("Restaurants")
    st.write("This page helps us to gain a basic understanding of the restaurants.")
    total_no_restaurants = query_executor.execute(
        sql="SELECT COUNT(DISTINCT place_id) as restaurant_count FROM restaurants",
        return_type="numpy",
    )
    text_str = (
        f"### Total number of unique restaurants: **"
        f"{str(total_no_restaurants['restaurant_count'][0])}**"
    )
    st.write(text_str)

    ## First row
    col1, col2 = st.columns(2)
    # offered payment methods
    payment_methods_df = query_executor.execute(sql.rpayment_methods)
    payment_methods_fig = bar_chart_cache(
        payment_methods_df, x="payment_method", y="count", title="Available Payment Methods"
    )
    col1.plotly_chart(payment_methods_fig, use_container_width=True)
    # offered cuisines
    cuisines_df = query_executor.execute(sql.rcuisines)
    cuisines_fig = bar_chart_cache(
        cuisines_df,
        x="cuisine",
        y="count",
        title="Offered Cuisines (more than 6 restaurants)",
    )
    col2.plotly_chart(cuisines_fig, use_container_width=True)

    ## Second row
    col1, col2 = st.columns(2)
    # top 5 best
    top_5_best_df = query_executor.execute(sql.top_five_best_restaurant)
    top_5_best_fig = restaurant_rating_cache(top_5_best_df, "Top 5 Best Rated Restaurants")
    col1.plotly_chart(top_5_best_fig, use_container_width=True)
    # top 5 worst
    top_5_worst_df = query_executor.execute(sql.top_five_worst_restaurant)
    top_5_worst_fig = restaurant_rating_cache(top_5_worst_df, "Top 5 Worst Rated Restaurants")
    col2.plotly_chart(top_5_worst_fig, use_container_width=True)

    # Third row
    col1, col2 = st.columns((1, 2))
    ctr = col1.container()
    # slider in container
    ctr.write("#")
    ctr.write("Slide to select random 5 restaurants within specified percentile:")
    x = ctr.slider(
        "Best to worst: 0 - 100",
        0,
        100,
        (20, 40),
        1,
    )
    # reselect another 5 results button in container
    ctr.write("####")
    reselect = ctr.button("Reselect")
    if reselect:
        random_5_percentile_df = query_executor.execute(
            sql=sql.random_five_restaurant_within_percentile,
            parameters=[
                x[0] / 100,
                x[1] / 100,
            ],
        )
    # not DRY but for initialization purpose
    random_5_percentile_df = query_executor.execute(
        sql=sql.random_five_restaurant_within_percentile,
        parameters=[
            x[0] / 100,
            x[1] / 100,
        ],
    )
    random_5_percentile_fig = restaurant_rating_cache(
        random_5_percentile_df,
        f"Random 5 Restaurants Within {x[0]} to {x[1]} Percentile",
    )
    col2.plotly_chart(random_5_percentile_fig, use_container_width=True)
    st.subheader("Restaurant Location")
    col1, col2 = st.columns((1, 1.25))
    # check box
    use_search = col2.checkbox("Use search input")
    # search bar
    search_restaurant = col1.text_input(
        "Enter exact restaurant name (case sensitive):", "emilianos"
    )  # give a default input
    profile_df = query_executor.execute(
        sql=sql.restaurant_profile,
        parameters=[search_restaurant],
    )
    # restaurant profile markdown
    md = generate_profile_md(profile_df)
    col1.markdown(md)

    # map
    if use_search:  # if use search then plot only one restaurant
        marker_size = (100, 125)
        restaurant_loc_df = query_executor.execute(
            sql=sql.restaurant_profile, parameters=[search_restaurant]
        )
        initial_view_one = pdk.ViewState(
            latitude=restaurant_loc_df["place_latitude"].iloc[0],
            longitude=restaurant_loc_df["place_longitude"].iloc[0],
            zoom=11,
            pitch=0,
        )
        map = restaurant_user_map(restaurant_loc_df, initial_view_one, marker_size)
    else:
        # select small > use search > exit use search > needs to display big marker size
        select_marker_size = col2.radio("Select marker size:", ("Big", "Small"))
        if select_marker_size == "Big":
            marker_size = (10000, 10000)
        else:
            marker_size = (100, 100)
        center_coord_df = query_executor.execute(
            """
            SELECT
                avg(place_latitude) as center_latitude,
                avg(place_longitude) as center_longitude
            FROM restaurants
        """
        )
        all_restaurant_loc_df = query_executor.execute(
            "SELECT place_latitude, place_longitude FROM restaurants"
        )
        initial_view_all = pdk.ViewState(
            latitude=center_coord_df["center_latitude"].iloc[0],
            longitude=center_coord_df["center_longitude"].iloc[0],
            zoom=5.5,
            pitch=0,
        )
        map = restaurant_user_map(all_restaurant_loc_df, initial_view_all, marker_size)
    map_container = col2.container()
    map_container.pydeck_chart(map, use_container_width=True)
    # use html to create legend
    map_container.markdown(map_legend, unsafe_allow_html=True)
