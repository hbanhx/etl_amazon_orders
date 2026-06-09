import logging
from builders.build_sales_order_payloads import build_sales_order_payloads
from application.fake_bc_client import post_sales_order_to_bc, post_sales_order_line_to_bc


def load_bc(headers_df, lines_df):
    logging.info("Starting load of sales orders to Fake BC")

    # Build payloads (list of tuples for each order: (header_payload, [line_payloads]))
    orders = build_sales_order_payloads(headers_df, lines_df)
    total_orders = len(orders)
    logging.info(f"Total orders to load: {total_orders}")

    for header_payload, line_payloads in orders:
        logging.info(f"Creating payload for order: {header_payload.get('External_Document_No')}")

        # Create order in BC and get order ID
        order = post_sales_order_to_bc(header_payload)
        order_id = order["id"]

        logging.debug(f"Order created in Fake BC with ID: {order_id}")

        # Create lines in BC for this returned order_id
        for line_payload in line_payloads:
            logging.debug(f"Creating line for order {order_id}: {line_payload}")
            
            post_sales_order_line_to_bc(order_id, line_payload)

        logging.debug(f"Finished sending lines for order {order_id}")
    
    logging.info("Finished loading all sales orders to Fake BC")