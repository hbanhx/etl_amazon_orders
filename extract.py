from sqlalchemy import create_engine, text, URL
import yaml




with open("config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

DATABASES = CONFIG["DATABASES"]
QUERIES = CONFIG["QUERIES"]


def create_url(db_config):
    connection_url = URL.create(
        drivername= DATABASES["am"]["drivername"],
        host= DATABASES["am"]["host"],
        database= DATABASES["am"]["database"],
        query= DATABASES["am"]["query"]
    )

    return connection_url


def build_engine(connection_url):
    engine = create_engine(connection_url)
    return engine

    


def extract():

    for db_name, db_config in DATABASES.items():
        connection_url = create_url(db_config)
        for key, sql_query in QUERIES[db_name].items():
            engine = build_engine(connection_url)
            
            with engine.connect() as conn:
                result = conn.execute(text(sql_query))
                raw_data = result.fetchall()

            return raw_data
       
extract()

# DATABASES: 
#   am:
#     # SQLAlchemy
#     driver: "mssql+pyodbc"
#     host: "localhost" # "DESKTOP-LQU6G64\\SQLEXPRESS"
#     db: "AM_DB"
#     query: {
#       "driver": "{ODBC Driver 17 for SQL Server}",
#       "TrustServerCertificate": "yes",
#       "Trusted_Connection": "yes",
#       }

# QUERIES:
#   am:
#     order:
#       SELECT *
#       FROM dbo.Orders





# def get_data():
#     pass
