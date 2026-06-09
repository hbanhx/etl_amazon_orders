import logging
import pandas as pd
from models.sales_header import SalesHeader


def build_sales_header_df(header_df):

    logging.info("Creating SalesHeader objects")

    sales_headers =  []
    for order_no, group in header_df.groupby("No"):
        row = group.iloc[0]
        sales_header = SalesHeader.from_row(row)
        sales_headers.append(sales_header)
    sales_headers_df = pd.DataFrame(sales_headers)

    logging.info(f"Sales headers created: {len(sales_headers)}")
    return sales_headers_df