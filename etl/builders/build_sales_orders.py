import logging
import pandas as pd
from models.sales_header import SalesHeader
from models.sales_line import SalesLine
# from application.fake_bc_client import create_sales_order, create_sales_order_line

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


def build_sales_line_df(lines_df):

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


def build_sales_order_payloads(headers_df, lines_df):
    # Build list of tuple payloads
    sales_order_payloads = []

    # Group lines by BC field "Document_No"
    lines_by_order = lines_df.groupby("Document_No")

    # Group headers by BC field "No"
    headers_by_order = headers_df.groupby("No")

    for order_no, header_group in headers_by_order:

        # Convert header row to dict
        header_row = header_group.iloc[0]
        header_payload = header_row.to_dict()

        # Get matching lines
        if order_no in lines_by_order.groups:
            order_lines_df = lines_by_order.get_group(order_no)
        else:
            order_lines_df = pd.DataFrame()

        # Convert lines to list of dicts
        line_payloads = []
        for _, row in order_lines_df.iterrows():
            line_payloads.append(row.to_dict())

        # Add to payloads as tuple
        sales_order_payloads.append((header_payload, line_payloads))

    return sales_order_payloads
