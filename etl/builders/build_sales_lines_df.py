import logging
import pandas as pd
from pandas import DataFrame
from models.sales_line import SalesLine


def build_sales_line_df(lines_df: DataFrame) -> DataFrame:

    logging.info("Creating SalesLine objects")

    sales_lines =  []
    for order_no, group in lines_df.groupby("Document_No"):
        line_no = 1000 # Reset per order
        for index, row in group.iterrows():
            sales_line = SalesLine.from_row(line_no, row)
            sales_lines.append(sales_line)
            line_no += 1000
    sales_lines_df = pd.DataFrame(sales_lines)

    logging.info(f"Sales lines created: {len(sales_lines)}")

    return sales_lines_df