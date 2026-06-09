import pandas as pd


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
