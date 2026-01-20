# -*- coding: utf-8 -*-
"""
pipeline
"""

import pipeline_functions as pf

print(f"******pipeline started******")

# Extract the data
apps_data = pf.extract("apps_data.csv")
reviews_data = pf.extract("review_data.csv")

print(f"******extract done******")

# Transform the data
top_apps_data = pf.transform(
    apps=apps_data,
    reviews=reviews_data,
    category="FOOD_AND_DRINK",
    min_rating=3.0,
    min_reviews=1000
)

print(f"******transform done******")

# Load the data
pf.load(
    dataframe=top_apps_data,
    database_name="market_research",
    table_name="top_apps"
)

print(f"******load done******")