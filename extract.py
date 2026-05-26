from sqlalchemy import create_engine, text, URL
import yaml
import pandas as pd




with open("config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

DATABASES = CONFIG["DATABASES"]
QUERIES = CONFIG["QUERIES"]


def create_url(db_name, db_config):
    connection_url = URL.create(
        drivername= db_config["drivername"],
        host= db_config["host"],
        database= db_config["database"],
        query= db_config["query"]
    )

    return connection_url

# https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine
def get_engine(connection_url):
    engine = create_engine(connection_url)
    return engine


def get_data():
    
    raw_data = {}
    for db_name, db_config in DATABASES.items():
        connection_url = create_url(db_name, db_config)
        
        for key, sql_query in QUERIES[db_name].items():
            engine = get_engine(connection_url)

            with engine.connect() as conn:
                raw_data[key] = pd.read_sql(sql_query, conn)
                print(raw_data[key])


    return raw_data


def extract():

     raw_data = get_data()


     return raw_data

extract()