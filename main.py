import logging
import os
from extract.extract import extract
from transform.transform import transform
# from load import load_data
import pandas as pd
from load.load_xlsx import load_xlsx

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "file.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


if __name__ == "__main__":
    logging.info("Starting ETL pipeline")

    raw_data = extract()
    print(raw_data.keys())

    data = transform(raw_data)
    
    load_xlsx(data)


    logging.info("ETL pipeline completed")