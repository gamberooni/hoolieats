# import re
# from typing import Dict, Tuple
# import pandas as pd
import plotly.express as px
import streamlit as st

# import plotly.graph_objects as go
# import pydeck as pdk


# def generate_profile_md(df):
#     business_hours_sub_pattern = r"\[|\]|'"
#     return f"""
#         ```
#         Name: {df['name'].iloc[0]}
#         Business Hours:
#             - Mon-Fri   : {re.sub(business_hours_sub_pattern, "", dict(df['business_hours'].iloc[0])['Mon-Fri'])}
#             - Sat       : {re.sub(business_hours_sub_pattern, "", dict(df['business_hours'].iloc[0])['Sat'])}
#             - Sun       : {re.sub(business_hours_sub_pattern, "", dict(df['business_hours'].iloc[0])['Sun'])}
#         Parking Lot: {', '.join(df['parking_lot'].iloc[0]).capitalize()}
#         Payment Method(s): {', '.join(df['payment_methods'].iloc[0]).capitalize().replace('_', ' ')}
#         Cuisine(s): {', '.join(df['cuisines'].iloc[0]).capitalize().replace('_', ' ')}
#         Address: {df['address'].iloc[0].title()}
#         City: {df['city'].iloc[0].title()}
#         State: {df['state'].iloc[0].title()}
#         Country: {df['country'].iloc[0].title()}
#         Zip: {df['zip'].iloc[0]}
#         Fax: {df['fax'].iloc[0]}
#         Alcohol: {df['alcohol'].iloc[0].capitalize().replace('_', '')}
#         Smoking Area: {df['smoking_area'].iloc[0].capitalize()}
#         Dress Code: {df['dress_code'].iloc[0].capitalize()}
#         Accessibility: {df['accessibility'].iloc[0].capitalize()}
#         Price: {df['price'].iloc[0].capitalize()}
#         URL: {df['url'].iloc[0]}
#         Ambience: {df['Rambience'].iloc[0].capitalize()}
#         Franchise: {df['franchise'].iloc[0].capitalize()}
#         Area: {df['area'].iloc[0].capitalize()}
#         Other Services: {df['other_services'].iloc[0].capitalize()}
#         ```
#     """


# def restaurant_user_map(restaurant_loc_df, initial_view, marker_size: Tuple):
#     user_loc_df = pd.read_sql_query(
#         "SELECT latitude, longitude FROM userprofile", con=engine
#     )
#     map = pdk.Deck(
#         map_style="mapbox://styles/mapbox/light-v9",
#         initial_view_state=initial_view,
#         layers=[
#             pdk.Layer(  # user location layer
#                 "ScatterplotLayer",
#                 user_loc_df,
#                 get_position=["longitude", "latitude"],
#                 auto_highlight=True,
#                 get_radius=marker_size[0],  # 125
#                 get_fill_color="[0, 0, 255, 100]",
#                 # pickable=True
#             ),
#             pdk.Layer(  # restaurant location layer
#                 "ScatterplotLayer",
#                 data=restaurant_loc_df,
#                 get_position="[longitude, latitude]",
#                 get_color="[255, 0, 0, 255]",
#                 get_radius=marker_size[1],  # 150
#             ),
#         ],
#     )
#     return map


# def plot_restaurant_rating(df, title: str):
#     fig = go.Figure(
#         data=[
#             go.Bar(
#                 name="Average Rating",
#                 x=df["name"],
#                 y=df["avg_rating"],
#                 yaxis="y",
#                 offsetgroup=1,
#             ),
#             go.Bar(
#                 name="Average Food Rating",
#                 x=df["name"],
#                 y=df["avg_food_rating"],
#                 yaxis="y",
#                 offsetgroup=2,
#             ),
#             go.Bar(
#                 name="Average Service Rating",
#                 x=df["name"],
#                 y=df["avg_service_rating"],
#                 yaxis="y",
#                 offsetgroup=3,
#             ),
#             go.Bar(
#                 name="Rating Count",
#                 x=df["name"],
#                 y=df["rating_count"],
#                 yaxis="y2",
#                 offsetgroup=4,
#             ),
#         ],
#         layout={
#             "title": title,
#             "xaxis": {"title": "Restaurant Name"},
#             "yaxis": {"title": "Rating Value"},
#             "yaxis2": {"title": "Rating Count", "overlaying": "y", "side": "right"},
#         },
#     )
#     # Change the bar mode to grouped
#     fig.update_layout(barmode="group", height=550)
#     return fig


# def plot_rating_facet(df, x_col, title: str, x_col_cat_order: Dict):
#     fig = px.bar(
#         df,
#         x=x_col,
#         y="count",
#         color="rating_value",
#         barmode="group",
#         facet_col="rating_type",
#         title=title,
#         category_orders={
#             "rating_type": ["rating", "food", "service"],
#             "rating_value": ["0", "1", "2"],
#         }.update(x_col_cat_order),
#     )
#     fig.update_layout(barmode="group", height=450)
#     return fig


# def plot_expected_rating_facet(
#     df, x_col, title: str, x_col_cat_order: Dict, dev_tol: int
# ):
#     fig = px.bar(
#         df,
#         x=x_col,
#         y="diff_pct",
#         color="rating_value",
#         barmode="group",
#         facet_col="rating_type",
#         title=title,
#         category_orders={
#             "rating_type": ["rating", "food", "service"],
#             "rating_value": ["0", "1", "2"],
#         }.update(x_col_cat_order),
#     )
#     fig.add_hrect(y0=0, y1=dev_tol, line_width=0, fillcolor="green", opacity=0.25)
#     fig.add_hrect(y0=0, y1=-dev_tol, line_width=0, fillcolor="green", opacity=0.25)
#     fig.update_layout(barmode="group", height=450)
#     return fig


# map_legend = """
#     <style>
#     .restaurant {{
#     height: 12px;
#     width: 12px;
#     background-color: #FF0000;
#     border-radius: 50%;
#     display: inline-block;
#     }}
#     .user {{
#     height: 12px;
#     width: 12px;
#     background-color: #0000FF;
#     opacity: 0.4;
#     border-radius: 50%;
#     display: inline-block;
#     }}
#     </style>
#     <div style="text-align:left">
#     <span class="restaurant"></span>  {}<br>
#     <span class="user"></span>  {}
#     </div>
#     """.format(
#     "Restaurant", "User"
# )


@st.cache(hash_funcs={dict: lambda _: None})  # hash_funcs because dict can't be hashed
def pie_chart_cache(df, names, title):
    fig = px.pie(df, values="count", names=names, title=title)
    fig.update_layout(height=450)
    return fig


# @st.cache(hash_funcs={dict: lambda _: None})
# def restaurant_rating_cache(df, title):
#     fig = plot_restaurant_rating(df, title)
#     return fig


@st.cache(hash_funcs={dict: lambda _: None})
def age_dist_cache(df):
    fig = px.histogram(df, x="age", title="Customer Age Distribution (as of 2011)")
    fig.update_layout(height=450)
    return fig


@st.cache(hash_funcs={dict: lambda _: None})
def bar_chart_cache(df, x, y, title):
    fig = px.bar(df, x=x, y=y, title=title)
    fig.update_traces(texttemplate="%{y}", textposition="outside")
    fig.update_layout(height=450)
    return fig


# @st.cache(hash_funcs={dict: lambda _: None})
# def rating_facet_cache(df, x_col, title, x_col_cat_order):
#     df["rating_value"] = df["rating_value"].astype(str)
#     fig = plot_rating_facet(df, x_col, title, x_col_cat_order)
#     fig.update_traces(texttemplate="%{y}", textposition="outside")
#     return fig


# @st.cache(hash_funcs={dict: lambda _: None})
# def expected_rating_facet_cache(df, x_col, title, x_col_cat_order, dev_tol):
#     df["rating_value"] = df["rating_value"].astype(str)
#     fig = plot_expected_rating_facet(df, x_col, title, x_col_cat_order, dev_tol)
#     fig.update_traces(texttemplate="%{y}", textposition="outside")
#     return fig
