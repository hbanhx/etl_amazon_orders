import logging
import os
from extract.extract import extract
from transform.transform import transform
from load.load_xlsx import load_xlsx
from load.load_sql import load_sql
from load.load_api import load_bc


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "file.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


if __name__ == "__main__":
    logging.info("Starting ETL pipeline")

    raw_data = extract()

    sales_headers_df, sales_lines_df, load_dfs = transform(raw_data)
    
    load_bc(sales_headers_df, sales_lines_df)
    load_xlsx(load_dfs)
    load_sql(sales_headers_df, sales_lines_df)

    logging.info("ETL pipeline completed")