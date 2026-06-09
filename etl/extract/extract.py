import os
from sqlalchemy import create_engine, URL
import yaml
import logging
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "config.yaml"))

with open(CONFIG_PATH, "r") as f:
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


def get_data(include_dbs):

    raw_data = {}
    for db_name, db_config in DATABASES.items():
        
        if db_name not in include_dbs:
            logging.info(f"Skipping database extract for: {db_name}")
            continue

        logging.info(f"Creating URL and engine for database: {db_name}")

        connection_url = create_url(db_config)
        engine = get_engine(connection_url)

        try:
            with engine.connect() as conn:
                for query_name, sql_query in QUERIES[db_name].items():
                    logging.info(f"Running query '{query_name}' on '{db_name}'")

                    raw_data[f"{db_name}_{query_name}"] = pd.read_sql(sql_query, conn)
                    
                    logging.info(f"Data extracted from: | database: {db_name} | query: {query_name}")

        except Exception as e:
            logging.error(f"Error occurred while extracting data from {db_name}: {e}")

        finally:
            engine.dispose()

    return raw_data

def extract():
    logging.info("Starting data extraction")

    extract_dbs = ["AM_DB"]
    raw_data = get_data(include_dbs=extract_dbs)

    logging.info(f"Extraction complete: {len(raw_data)} datasets loaded")
    return raw_data