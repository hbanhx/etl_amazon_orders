import os
from sqlalchemy import create_engine, URL
import yaml
import logging
import pandas as pd
from pandas import DataFrame

# https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "config.yaml"))

with open(CONFIG_PATH, "r") as f:
    CONFIG = yaml.safe_load(f)

DATABASES = CONFIG["DATABASES"]
QUERIES = CONFIG["QUERIES"]


def create_url(db_config: dict) -> URL:
    connection_url = URL.create(
        drivername= db_config["drivername"],
        host= db_config["host"],
        database= db_config["database"],
        query= db_config["query"]
    )

    return connection_url


def load_data(include_dbs: list, df: DataFrame, table_name: str) -> None:
    
    for db_name, db_config in DATABASES.items():
        
        if db_name not in include_dbs:
            logging.info(f"Skipping load to SQL: | database: {db_name}")
            continue

        logging.info(f"Creating URL and engine for SQL: | database: {db_name}")

        connection_url = create_url(db_config)
        engine = create_engine(connection_url)

        logging.info(f"Loading table '{table_name}' into SQL: | database: {db_name}")
        
        try:
            with engine.connect() as conn:
                df.to_sql(table_name, conn, if_exists="replace", index=False)

                logging.info(f"Data loaded to SQL: | database: {db_name} | table name: {table_name}")
        
        except Exception as e:
            logging.error(f"Error loading into {db_name}.{table_name}: {e}")

        finally:
            engine.dispose()


def load_sql(sales_headers_df: DataFrame, sales_lines_df: DataFrame) -> None:
    logging.info("Starting data load to SQL database")

    load_to_dbs = ["GS_DB"]

    load_data(include_dbs=load_to_dbs, df=sales_headers_df, table_name="salesHeader")
    load_data(include_dbs=load_to_dbs, df=sales_lines_df, table_name="salesLine")
    
    logging.info(f"Data load to SQL database complete")
