# import pandas as pd
# import streamlit as st
# from config.config import engine
# from sql.rating_behavior_sql import *
# from utils.common import calc_diff
# from utils.plot_utils import *
# def app():
#     st.title("Customer Rating Behavior")
#     st.write(
#         "This page helps us to gain insights on the rating behavior of the customers."
#     )
#     total_ratings_given = pd.read_sql_query("SELECT COUNT(*) FROM rbview", con=engine)[
#         "count"
#     ].iloc[0]
#     st.write("### Total number of ratings given: **" + str(total_ratings_given) + "**")
#     col1, col2, col3 = st.columns(3)
#     # food rating count
#     food_rating_cnt_df = pd.read_sql_query(food_rating_count, con=engine)
#     food_rating_cnt_fig = pie_chart_cache(
#         food_rating_cnt_df, names="food_rating", title="Food Rating Count"
#     )
#     food_rating_cnt_fig.update_layout(height=400)
#     col1.plotly_chart(food_rating_cnt_fig, use_container_width=True)
#     # rating count
#     rating_cnt_df = pd.read_sql_query(rating_count, con=engine)
#     rating_cnt_fig = pie_chart_cache(
#         rating_cnt_df, names="rating", title="Rating Count"
#     )
#     rating_cnt_fig.update_layout(height=400)
#     col2.plotly_chart(rating_cnt_fig, use_container_width=True)
#     # service rating count
#     service_rating_cnt_df = pd.read_sql_query(service_rating_count, con=engine)
#     service_rating_cnt_fig = pie_chart_cache(
#         service_rating_cnt_df, names="service_rating", title="Service Rating Count"
#     )
#     service_rating_cnt_fig.update_layout(height=400)
#     col3.plotly_chart(service_rating_cnt_fig, use_container_width=True)
#     st.write(
#         "Rating and food rating have rating value of 2 as the highest occurrence, \
#         followed by rating value of 1 and 0. For service rating, rating value of 1 is the highest. \
#         We should expect to see this pattern in all the criteria below. \
#         Any criterion that deviates from this pattern for more than a threshold \
#         (i.e. **deviation tolerance**), for e.g., 10%, should be marked as interesting."
#     )
#     st.write(
#         "Positive difference in percentage means that the actual count is more than the expected count and vice versa."
#     )
#     st.write("##")  # for spacing
#     col1, col2, col3 = st.columns((0.75, 0.5, 1.25))
#     dev_tol = col1.number_input(
#         "Deviation Tolerance (postive numbers only)", 0, value=10, step=1, format="%d"
#     )  # default 10% deviation tolerance
#     col3.write(
#         "To calculate the expected count using actual count and difference in percentage:"
#     )
#     col3.latex(r""" expected = actual\times \frac{1-diffpct}{100} """)
#     st.write("#")  # for spacing
#     # calculate the percentage distribution of the rating values of each rating type
#     rating_cnt_df["expected_pct"] = round(
#         rating_cnt_df["count"] / rating_cnt_df["count"].sum(), 3
#     )
#     food_rating_cnt_df["expected_pct"] = round(
#         food_rating_cnt_df["count"] / food_rating_cnt_df["count"].sum(), 3
#     )
#     service_rating_cnt_df["expected_pct"] = round(
#         service_rating_cnt_df["count"] / service_rating_cnt_df["count"].sum(), 3
#     )
#     # offered and preferred cuisines
#     # has null values that are not plotted because some rows from "rcuisine" are null
#     st.write(
#         "**1. Does it affect behavior rating when the customer's preferred cuisine is/is not \
#             offered by the restaurant?**"
#     )
#     col1, col2 = st.columns(2)
#     cuisines_df = pd.read_sql_query(cuisines, con=engine)
#     cuisines_diff_df = calc_diff(
#         cuisines_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "offered",
#         [False, True],
#     )
#     cuisines_fig = rating_facet_cache(
#         cuisines_diff_df,
#         "offered",
#         "Cuisines (at least 1 offered)",
#         {"offered": ["false", "true"]},
#     )
#     cuisines_expected_fig = expected_rating_facet_cache(
#         cuisines_diff_df,
#         "offered",
#         "Difference in Percentage",
#         {"offered": ["false", "true"]},
#         dev_tol,
#     )
#     col1.plotly_chart(cuisines_fig, use_container_width=True)
#     col2.plotly_chart(cuisines_expected_fig, use_container_width=True)
#     # offered and preferred payment methods
#     st.write(
#         "**2. Does it affect behavior rating when the customer's possessed payment method is/is not \
#             offered by the restaurant?**"
#     )
#     col1, col2 = st.columns(2)
#     payment_methods_df = pd.read_sql_query(payment_methods, con=engine)
#     payment_methods_diff_df = calc_diff(
#         payment_methods_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "offered",
#         [False, True],
#     )
#     payment_methods_fig = rating_facet_cache(
#         payment_methods_diff_df,
#         "offered",
#         "Payment Methods (at least 1 offered)",
#         {"offered": ["false", "true"]},
#     )
#     payment_methods_expected_fig = expected_rating_facet_cache(
#         payment_methods_diff_df,
#         "offered",
#         "Difference in Percentage",
#         {"offered": ["false", "true"]},
#         dev_tol,
#     )
#     col1.plotly_chart(payment_methods_fig, use_container_width=True)
#     col2.plotly_chart(payment_methods_expected_fig, use_container_width=True)
#     # restaurant accessibility
#     st.write(
#         "**3. Does it affect behavior rating when the restaurant offers no/partial/complete \
#             accessibility to special needs invididuals?**"
#     )
#     col1, col2 = st.columns(2)
#     raccessibility_df = pd.read_sql_query(raccessibility, con=engine)
#     raccessibility_diff_df = calc_diff(
#         raccessibility_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "raccessibility",
#         ["partially", "no_accessibility", "completely"],
#     )
#     raccessibility_fig = rating_facet_cache(
#         raccessibility_df,
#         "raccessibility",
#         "Restaurant Accessibility",
#         {"raccessibility": ["partially", "no_accessibility", "completely"]},
#     )
#     raccessibility_expected_fig = expected_rating_facet_cache(
#         raccessibility_diff_df,
#         "raccessibility",
#         "Difference in Percentage",
#         {"raccessibility": ["partially", "no_accessibility", "completely"]},
#         dev_tol,
#     )
#     col1.plotly_chart(raccessibility_fig, use_container_width=True)
#     col2.plotly_chart(raccessibility_expected_fig, use_container_width=True)
#     # restaurant is open/closed area
#     st.write(
#         "**4. Does it affect behavior rating when it is an open area or a closed area restaurant?**"
#     )
#     col1, col2 = st.columns(2)
#     rarea_df = pd.read_sql_query(rarea, con=engine)
#     rarea_diff_df = calc_diff(
#         rarea_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "rarea",
#         ["open", "closed"],
#     )
#     rarea_fig = rating_facet_cache(
#         rarea_df,
#         "rarea",
#         "Restaurant Is Open/Closed Area",
#         {"rarea": ["open", "closed"]},
#     )
#     rarea_expected_fig = expected_rating_facet_cache(
#         rarea_diff_df,
#         "rarea",
#         "Difference in Percentage",
#         {"rarea": ["open", "closed"]},
#         dev_tol,
#     )
#     col1.plotly_chart(rarea_fig, use_container_width=True)
#     col2.plotly_chart(rarea_expected_fig, use_container_width=True)
#     # restaurant provides other services
#     st.write(
#         "**5. Does it affect behavior rating when the restaurant offers or does not offer \
#             internet and/or a variety of other services?**"
#     )
#     col1, col2 = st.columns(2)
#     rother_services_df = pd.read_sql_query(rother_services, con=engine)
#     rother_services_diff_df = calc_diff(
#         rother_services_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "rother_services",
#         ["none", "variety", "Internet"],
#     )
#     rother_services_fig = rating_facet_cache(
#         rother_services_df,
#         "rother_services",
#         "Restaurant Has Other Services",
#         {"rother_services": ["none", "variety", "Internet"]},
#     )
#     rother_services_expected_fig = expected_rating_facet_cache(
#         rother_services_diff_df,
#         "rother_services",
#         "Difference in Percentage",
#         {"rother_services": ["none", "variety", "Internet"]},
#         dev_tol,
#     )
#     col1.plotly_chart(rother_services_fig, use_container_width=True)
#     col2.plotly_chart(rother_services_expected_fig, use_container_width=True)
#     # restaurant is a franchise
#     st.write(
#         "**6. Does it affect behavior rating when the restaurant is a franchise?**"
#     )
#     col1, col2 = st.columns(2)
#     rfranchise_df = pd.read_sql_query(rfranchise, con=engine)
#     rfranchise_df["rfranchise"] = rfranchise_df["rfranchise"].replace({"f": "false"})
#     rfranchise_df["rfranchise"] = rfranchise_df["rfranchise"].replace({"t": "true"})
#     rfranchise_diff_df = calc_diff(
#         rfranchise_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "rfranchise",
#         ["false", "true"],
#     )
#     rfranchise_fig = rating_facet_cache(
#         rfranchise_df,
#         "rfranchise",
#         "Restaurant Is Franchise",
#         {"rfranchise": ["false", "true"]},
#     )
#     rfranchise_expected_fig = expected_rating_facet_cache(
#         rfranchise_diff_df,
#         "rfranchise",
#         "Difference in Percentage",
#         {"rfranchise": ["false", "true"]},
#         dev_tol,
#     )
#     col1.plotly_chart(rfranchise_fig, use_container_width=True)
#     col2.plotly_chart(rfranchise_expected_fig, use_container_width=True)
#     # is smoking allowed in restaurant
#     st.write(
#         "**7. Does it affect behavior rating when the restaurant allows smoking?**"
#     )
#     col1, col2 = st.columns(2)
#     smoking_allowed_df = pd.read_sql_query(smoking_allowed, con=engine)
#     smoking_allowed_df = smoking_allowed_df.rename(
#         columns={"rsmoking_allowed": "allowed"}
#     )
#     smoking_allowed_diff_df = calc_diff(
#         smoking_allowed_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "allowed",
#         ["false", "true"],
#     )
#     smoking_allowed_fig = rating_facet_cache(
#         smoking_allowed_df,
#         "allowed",
#         "Restaurant Smoking Allowed",
#         {"allowed": ["false", "true"]},
#     )
#     rfranchise_expected_fig = expected_rating_facet_cache(
#         smoking_allowed_diff_df,
#         "allowed",
#         "Difference in Percentage",
#         {"allowed": ["false", "true"]},
#         dev_tol,
#     )
#     col1.plotly_chart(smoking_allowed_fig, use_container_width=True)
#     col2.plotly_chart(rfranchise_expected_fig, use_container_width=True)
#     # restaurant price meets customer budget
#     st.write(
#         "**8. Does it affect behavior rating when the restaurant price meets the customer's budget?**"
#     )
#     col1, col2 = st.columns(2)
#     price_budget_matched_df = pd.read_sql_query(price_budget_matched, con=engine)
#     price_budget_matched_df = price_budget_matched_df.rename(
#         columns={"price_budget_matched": "matched"}
#     )
#     price_budget_matched_diff_df = calc_diff(
#         price_budget_matched_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "matched",
#         ["N/A", "false", "true"],
#     )
#     price_budget_matched_fig = rating_facet_cache(
#         price_budget_matched_df,
#         "matched",
#         "Restaurant Price Meets Customer Budget",
#         {"matched": ["N/A", "false", "true"]},
#     )
#     price_budget_matched_diff_fig = expected_rating_facet_cache(
#         price_budget_matched_diff_df,
#         "matched",
#         "Difference in Percentage",
#         {"matched": ["N/A", "false", "true"]},
#         dev_tol,
#     )
#     col1.plotly_chart(price_budget_matched_fig, use_container_width=True)
#     col2.plotly_chart(price_budget_matched_diff_fig, use_container_width=True)
#     # restaurant offers alcohol
#     st.write(
#         "**9. Does it affect behavior rating when the restaurant offers alcohol?**"
#     )
#     col1, col2 = st.columns(2)
#     ralcohol_df = pd.read_sql_query(ralcohol, con=engine)
#     ralcohol_diff_df = calc_diff(
#         ralcohol_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "ralcohol",
#         ["No_Alcohol_Served", "Wine-Beer", "Full_Bar"],
#     )
#     ralcohol_fig = rating_facet_cache(
#         ralcohol_df,
#         "ralcohol",
#         "Restaurant Offers Alcohol",
#         {"ralcohol": ["No_Alcohol_Served", "Wine-Beer", "Full_Bar"]},
#     )
#     ralcohol_diff_fig = expected_rating_facet_cache(
#         ralcohol_diff_df,
#         "ralcohol",
#         "Difference in Percentage",
#         {"ralcohol": ["No_Alcohol_Served", "Wine-Beer", "Full_Bar"]},
#         dev_tol,
#     )
#     col1.plotly_chart(ralcohol_fig, use_container_width=True)
#     col2.plotly_chart(ralcohol_diff_fig, use_container_width=True)
#     # restaurant has url
#     st.write("**10. Does it affect behavior rating when the restaurant has URL?**")
#     col1, col2 = st.columns(2)
#     rhas_url_df = pd.read_sql_query(rhas_url, con=engine)
#     rhas_url_diff_df = calc_diff(
#         rhas_url_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "rhas_url",
#         ["false", "true"],
#     )
#     rhas_url_fig = rating_facet_cache(
#         rhas_url_df, "rhas_url", "Restaurant Has URL", {"rhas_url": ["false", "true"]}
#     )
#     rhas_url_diff_fig = expected_rating_facet_cache(
#         rhas_url_diff_df,
#         "rhas_url",
#         "Difference in Percentage",
#         {"rhas_url": ["false", "true"]},
#         dev_tol,
#     )
#     col1.plotly_chart(rhas_url_fig, use_container_width=True)
#     col2.plotly_chart(rhas_url_diff_fig, use_container_width=True)
#     # customer parking lot needs fulfilled
#     st.write(
#         "**11. Does it affect behavior rating when the customer's parking lot needs are fulfilled?**"
#     )
#     col1, col2 = st.columns(2)
#     parking_needs_fulfilled_df = pd.read_sql_query(parking_needs_fulfilled, con=engine)
#     parking_needs_fulfilled_diff_df = calc_diff(
#         parking_needs_fulfilled_df,
#         rating_cnt_df,
#         service_rating_cnt_df,
#         food_rating_cnt_df,
#         "fulfilled",
#         ["false", "true"],
#     )
#     parking_needs_fulfilled_fig = rating_facet_cache(
#         parking_needs_fulfilled_df,
#         "fulfilled",
#         "Customer Parking Needs Fulfilled",
#         {"fulfilled": ["false", "true"]},
#     )
#     parking_needs_fulfilled_diff_fig = expected_rating_facet_cache(
#         parking_needs_fulfilled_diff_df,
#         "fulfilled",
#         "Difference in Percentage",
#         {"fulfilled": ["false", "true"]},
#         dev_tol,
#     )
#     col1.plotly_chart(parking_needs_fulfilled_fig, use_container_width=True)
#     col2.plotly_chart(parking_needs_fulfilled_diff_fig, use_container_width=True)
