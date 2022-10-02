import streamlit as st
from utils.plot_utils import *

from hoolieats import query_executor


def app():
    st.title("Customers")
    st.write("This page helps us to gain a basic understanding of the customers.")

    total_no_customers = query_executor.execute(
        sql="select count(distinct user_id) as user_count from users",
        return_type="numpy",
    )
    st.write(
        "### Total number of unique customers: **" + str(total_no_customers["user_count"][0]) + "**"
    )

    ## First row
    col1, col2 = st.columns(2)
    # age distribution
    age_dist_df = query_executor.execute("select age from users")
    age_dist_fig = age_dist_cache(age_dist_df)
    col1.plotly_chart(age_dist_fig, use_container_width=True)
    # bmi
    bmi_df = age_dist_df = query_executor.execute(
        "select count(*) as count, bmi_status from users group by bmi_status"
    )
    bmi_fig = bar_chart_cache(bmi_df, x="bmi_status", y="count", title="BMI Status")
    col2.plotly_chart(bmi_fig, use_container_width=True)

    # ## Second row
    # col1, col2 = st.columns(2)
    # # payment methods
    # payment_methods_df = pd.read_sql_query(
    #     customer_available_payment_methods, con=engine
    # )
    # payment_methods_fig = bar_chart_cache(
    #     payment_methods_df, x="Upayment", y="count", title="Possessed Payment Methods"
    # )
    # col1.plotly_chart(payment_methods_fig, use_container_width=True)
    # # preferred cuisines
    # cuisines_df = pd.read_sql_query(customer_preferred_cuisines, con=engine)
    # cuisines_fig = bar_chart_cache(
    #     cuisines_df,
    #     x="Rcuisine",
    #     y="count",
    #     title="Customer Preferred Cuisines (more than 1 customer)",
    # )
    # col2.plotly_chart(cuisines_fig, use_container_width=True)

    # ## Third row
    # col1, col2, col3 = st.columns(3)
    # # marital status
    # marital_status_df = pd.read_sql_query(customer_marital_status, con=engine)
    # marital_status_fig = pie_chart_cache(
    #     marital_status_df, names="marital_status", title="Marital Status"
    # )
    # marital_status_fig.update_layout(height=400)
    # col1.plotly_chart(marital_status_fig, use_container_width=True)
    # # color
    # color_df = pd.read_sql_query(customer_color, con=engine)
    # color_fig = pie_chart_cache(color_df, names="color", title="Color")
    # color_fig.update_layout(height=400)
    # col2.plotly_chart(color_fig, use_container_width=True)
    # # smoker
    # smoker_df = pd.read_sql_query(customer_is_smoker, con=engine)
    # smoker_fig = pie_chart_cache(smoker_df, names="smoker", title="Is Smoker")
    # smoker_fig.update_layout(height=400)
    # col3.plotly_chart(smoker_fig, use_container_width=True)

    # ## Fourth row
    # col1, col2, col3 = st.columns(3)
    # # drink level
    # drink_level_df = pd.read_sql_query(customer_drink_level, con=engine)
    # drink_level_fig = pie_chart_cache(
    #     drink_level_df, names="drink_level", title="Drink Level"
    # )
    # drink_level_fig.update_layout(height=400)
    # col1.plotly_chart(drink_level_fig, use_container_width=True)
    # # dress preference
    # dress_pref_df = pd.read_sql_query(customer_dress_preference, con=engine)
    # dress_pref_fig = pie_chart_cache(
    #     dress_pref_df, names="dress_preference", title="Dress Preference"
    # )
    # dress_pref_fig.update_layout(height=400)
    # col2.plotly_chart(dress_pref_fig, use_container_width=True)
    # # ambience
    # ambience_df = pd.read_sql_query(customer_ambience, con=engine)
    # ambience_fig = pie_chart_cache(ambience_df, names="ambience", title="Ambience")
    # ambience_fig.update_layout(height=400)
    # col3.plotly_chart(ambience_fig, use_container_width=True)

    # ## Fifth row
    # col1, col2, col3 = st.columns(3)
    # # hijos
    # hijos_df = pd.read_sql_query(customer_hijos, con=engine)
    # hijos_fig = pie_chart_cache(hijos_df, names="hijos", title="Hijos")
    # hijos_fig.update_layout(height=400)
    # col1.plotly_chart(hijos_fig, use_container_width=True)
    # # activity
    # activity_df = pd.read_sql_query(customer_activity, con=engine)
    # activity_fig = pie_chart_cache(activity_df, names="activity", title="Activity")
    # activity_fig.update_layout(height=400)
    # col2.plotly_chart(activity_fig, use_container_width=True)
    # # personality
    # personality_df = pd.read_sql_query(customer_personality, con=engine)
    # personality_fig = pie_chart_cache(
    #     personality_df, names="personality", title="Personality"
    # )
    # personality_fig.update_layout(height=400)
    # col3.plotly_chart(personality_fig, use_container_width=True)

    # ## Sixth row
    # col1, col2 = st.columns(2)
    # # budget
    # budget_df = pd.read_sql_query(customer_budget, con=engine)
    # budget_fig = pie_chart_cache(budget_df, names="budget", title="Budget")
    # budget_fig.update_layout(height=400)
    # col1.plotly_chart(budget_fig, use_container_width=True)
    # # religion
    # religion_df = pd.read_sql_query(customer_religion, con=engine)
    # religion_fig = pie_chart_cache(religion_df, names="religion", title="Religion")
    # religion_fig.update_layout(height=400)
    # col2.plotly_chart(religion_fig, use_container_width=True)
