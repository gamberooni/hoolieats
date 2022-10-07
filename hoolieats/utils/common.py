from typing import List


def calc_diff(
    df,
    rating_cnt_df,
    service_rating_cnt_df,
    food_rating_cnt_df,
    categorical_col: str,
    categories: List,
):
    # use a dict to have the following information:
    # {'service': [index locations], 'food': [index locations], 'rating': [index locations]}
    # index locations are filtered based on the number of categories in the categorical column
    # index locations are pandas df masks (False and True to indicate with rows to pick)
    idx_hashmap = {}
    for rating_type in ["service", "food", "rating"]:
        idx_hashmap[rating_type] = []
        for c in categories:
            idx_hashmap[rating_type].append(
                ((df["rating_type"] == rating_type) & (df[categorical_col] == c))
            )

    # use the dict to calculate the expected rating count for each rating value (0, 1, 2) & category
    # using cuisines df as example, the categorical column is "offered"
    #   and the categories are True/False
    # the combination is - [rating type, rating value, categories]
    # [rating, 0, False]
    # [rating, 1, False]
    # [rating, 2, False]  - these 3 rows belong to a group
    #   i.e. should follow the expected distribution for rating type = "rating"
    #   as shown in the pie chart
    # [rating, 0, True]
    # [rating, 1, True]
    # [rating, 2, True]  - these 3 rows belong to another group
    #   should follow the rating type = "rating" pattern too
    # ...
    # using the original df, for rating_type = "rating", filter out the rows with rating value = 0
    #   and category = False
    # then assign the expected percentage on the row where rating value = 0 and category = False
    # then calculate the expected count based on the sum of all the rows where
    #   rating type = "rating", rating value = 0, 1, 2 and category = False
    # repeat for the remaining conditions
    for rating_type, idx_list in idx_hashmap.items():
        for value in [0, 1, 2]:
            if rating_type == "rating":
                for i in idx_list:
                    df.loc[
                        i & (df["rating_value"] == value), "expected_pct_by_type"
                    ] = rating_cnt_df.loc[rating_cnt_df["rating"] == value, "expected_pct"].iloc[0]
                    df.loc[i, "expected_count_by_type"] = (
                        df[i]["count"].sum() * df.loc[i, "expected_pct_by_type"]
                    )
            elif rating_type == "service":
                for i in idx_list:
                    df.loc[
                        i & (df["rating_value"] == value), "expected_pct_by_type"
                    ] = service_rating_cnt_df.loc[
                        service_rating_cnt_df["service_rating"] == value, "expected_pct"
                    ].iloc[
                        0
                    ]
                    df.loc[i, "expected_count_by_type"] = (
                        df[i]["count"].sum() * df.loc[i, "expected_pct_by_type"]
                    )
            elif rating_type == "food":
                for i in idx_list:
                    df.loc[
                        i & (df["rating_value"] == value), "expected_pct_by_type"
                    ] = food_rating_cnt_df.loc[
                        food_rating_cnt_df["food_rating"] == value, "expected_pct"
                    ].iloc[
                        0
                    ]
                    df.loc[i, "expected_count_by_type"] = (
                        df[i]["count"].sum() * df.loc[i, "expected_pct_by_type"]
                    )

    df["diff_pct"] = round((df["count"] - df["expected_count_by_type"]) / df["count"] * 100, 1)
    return df
