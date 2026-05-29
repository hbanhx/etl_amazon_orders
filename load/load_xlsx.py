import logging
import os



def load_xlsx(load_data):

    logging.info("Starting data load to Excel file")

    df = load_data["orders"]
    dir = "output"
    name = "orders"
    print(df.dtypes)

    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = os.path.join(base, f"{dir}")
    os.makedirs(dir_path, exist_ok=True)
    path = os.path.join(dir_path, f"{name}.xlsx")
    df.to_excel(path, index=False)



    logging.info("Data load complete")
