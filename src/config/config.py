import os

from sqlalchemy import create_engine

DATA_FOLDER = os.path.join(os.getcwd(), "RCdata")
chefmozaccepts_file = os.path.join(DATA_FOLDER, "chefmozaccepts.csv")
chefmozcuisine_file = os.path.join(DATA_FOLDER, "chefmozcuisine.csv")
chefmozhours4_file = os.path.join(DATA_FOLDER, "chefmozhours4.csv")
chefmozparking_file = os.path.join(DATA_FOLDER, "chefmozparking.csv")
geoplaces2_file = os.path.join(DATA_FOLDER, "geoplaces2.csv")
usercuisine_file = os.path.join(DATA_FOLDER, "usercuisine.csv")
userpayment_file = os.path.join(DATA_FOLDER, "userpayment.csv")
userprofile_file = os.path.join(DATA_FOLDER, "userprofile.csv")
rating_final_file = os.path.join(DATA_FOLDER, "rating_final.csv")

postgres_host = os.environ["POSTGRES_HOST"]
postgres_user = os.environ["POSTGRES_USER"]
postgres_password = os.environ["POSTGRES_PASSWORD"]
postgres_port = os.environ["POSTGRES_PORT"]
postgres_database = os.environ["POSTGRES_DATABASE"]

engine = create_engine(
    f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}"
)
