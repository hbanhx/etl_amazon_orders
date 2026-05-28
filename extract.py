from sqlalchemy import create_engine, URL
import yaml
import logging
import pandas as pd

with open("config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

DATABASES = CONFIG["DATABASES"]
QUERIES = CONFIG["QUERIES"]


def create_url(db_config):
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
        logging.info(f"Creating URL and engine for database: {db_name}")


        connection_url = create_url(db_config)
        engine = get_engine(connection_url)


        for query_name, sql_query in QUERIES[db_name].items():
            logging.info(f"Running query '{query_name}' on '{db_name}'")

            with engine.connect() as conn:
                raw_data[query_name] = pd.read_sql(sql_query, conn)
                print(raw_data[query_name].info())
                logging.info(f"Data extracted from: | database: {db_name} | query: {query_name}")

    return raw_data

def extract():
    logging.info("Starting data extraction")
    raw_data = get_data()

    
    logging.info(f"Extraction complete: {len(raw_data)} datasets loaded")
    return raw_data