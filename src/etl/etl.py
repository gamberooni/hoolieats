import os
import sys

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

import pandas as pd

import os
from sql.etl_sql import *
from config.config import *
from utils.common import init_postgres_conn, psql_insert_copy, split_hours


def main():
    conn = init_postgres_conn(
        postgres_host,
        postgres_port,
        postgres_database,
        postgres_user,
        postgres_password,
    )
    cur = conn.cursor()

    # E(T)L for each file
    # restaurants
    chefmozaccepts_df = pd.read_csv(chefmozaccepts_file)
    # simple transformation
    # chefmozaccepts_df["Rpayment"] = chefmozaccepts_df["Rpayment"].replace(
    #     {"Visa": "VISA"}
    # )
    chefmozaccepts_df = chefmozaccepts_df.fillna(value="N/A")
    chefmozaccepts_df.to_sql(
        "chefmozaccepts",
        engine,
        if_exists="replace",
        index=False,
        method=psql_insert_copy,
    )

    chefmozcuisine_df = pd.read_csv(chefmozcuisine_file)
    chefmozcuisine_df.to_sql(
        "chefmozcuisine",
        engine,
        if_exists="replace",
        index=False,
        method=psql_insert_copy,
    )

    chefmozhours4_df = pd.read_csv(chefmozhours4_file)
    # simple transformation
    chefmozhours4_df = (
        chefmozhours4_df.drop_duplicates()
    )  # there are duplicates in the csv
    # chefmozhours4_df["days"] = chefmozhours4_df["days"].replace(
    #     {"Mon;Tue;Wed;Thu;Fri;": "Mon-Fri"}
    # )
    # chefmozhours4_df[["hours", "days"]] = chefmozhours4_df[["hours", "days"]].replace(
    #     {";": ""}, regex=True
    # )
    chefmozhours4_df = (
        chefmozhours4_df.groupby(["placeID", "days"])["hours"]
        .agg("".join)
        .reset_index()
    )
    # chefmozhours4_df["hours"] = chefmozhours4_df["hours"].map(split_hours)
    chefmozhours4_df.to_sql(
        "chefmozhours4",
        engine,
        if_exists="replace",
        index=False,
        method=psql_insert_copy,
    )

    chefmozparking_df = pd.read_csv(chefmozparking_file)
    chefmozparking_df.to_sql(
        "chefmozparking",
        engine,
        if_exists="replace",
        index=False,
        method=psql_insert_copy,
    )

    geoplaces2_df = pd.read_csv(geoplaces2_file, encoding="latin-1")
    # replace ? with N/A
    geoplaces2_df = geoplaces2_df.replace({"?": "N/A"})
    geoplaces2_df.to_sql(
        "geoplaces2", engine, if_exists="replace", index=False, method=psql_insert_copy
    )

    # users
    usercuisine_df = pd.read_csv(usercuisine_file)
    usercuisine_df.to_sql(
        "usercuisine", engine, if_exists="replace", index=False, method=psql_insert_copy
    )

    userpayment_df = pd.read_csv(userpayment_file)
    userpayment_df.to_sql(
        "userpayment", engine, if_exists="replace", index=False, method=psql_insert_copy
    )

    userprofile_df = pd.read_csv(userprofile_file)
    userprofile_df = userprofile_df.replace({"?": "N/A"})
    userprofile_df.to_sql(
        "userprofile", engine, if_exists="replace", index=False, method=psql_insert_copy
    )

    # ratings
    rating_final_df = pd.read_csv(rating_final_file)
    rating_final_df.to_sql(
        "rating_final",
        engine,
        if_exists="replace",
        index=False,
        method=psql_insert_copy,
    )

    # create views for easier sql queries in streamlit
    cur.execute(f"CREATE VIEW rview AS {restaurant_view}")
    cur.execute(f"CREATE VIEW cview AS {customer_view}")
    cur.execute(f"CREATE VIEW rbview_tmp AS {rating_behavior_view}")
    cur.execute(rhas_parking_lot)  # create view from the rbview_tmp
    conn.commit()

    print("Completed ETL and written data to Postgres")


if __name__ == "__main__":
    main()
