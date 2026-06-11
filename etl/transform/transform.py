import logging
import pandas as pd
import numpy as np
from pandas import DataFrame
from mappings.mappings import Mappings
from builders.build_sales_headers_df import build_sales_header_df
from builders.build_sales_lines_df import build_sales_line_df


def extract_to_transform(raw_data: dict) -> DataFrame:
    logging.info("Extracting Amazon orders from raw_data")
    return raw_data["AM_DB_am_orders"]

def prepare_amazon_order(am_orders_df: DataFrame) -> tuple[DataFrame, DataFrame, DataFrame]:
    logging.info(f"Preparing Amazon orders: {len(am_orders_df)} rows received")

    data = am_orders_df.copy()

    # Unit price calculation
    data["Unit_Price"] = (
        data["vat-exclusive-item-price"]
        + data["shipping-price"]
        - data["shipping-tax"]
        + data["gift-wrap-price"]
        - data["gift-wrap-tax"]
        - data["item-promotion-discount"]
        - data["ship-promotion-discount"]
        )
    
    # VAT percentage calculation
    data["vat_pct"] = (data["item-tax"] / data["Unit_Price"].replace(0, np.nan)).round(2)

    # Determine Sell_to_Customer_No based on VAT percentage and buyer tax registration id
    data["Sell_to_Customer_No"] = None
    data.loc[(data["vat_pct"].isna() | data["vat_pct"] == 0) & data["buyer-tax-registration-id"].notna(), "Sell_to_Customer_No"] = "CUS1025197"
    data.loc[data["vat_pct"] == 0.19, "Sell_to_Customer_No"] = "CUS1002096"

    # Flag valid orders
    data["is_valid_amazon_de_order"] = (
        (data["is-amazon-invoiced"] == True)
        & (data["order-status"] == "Shipped")
        & (data["sales-channel"] == "Amazon.de")
        & (data["vat_pct"].isin([0, 0.19]))
        & (data["currency"] == "EUR")
        & (~data["buyer-tax-registration-id"].str.contains(",", na=False))
        & (data["Sell_to_Customer_No"].notna())
    )

    # Flag invalid orders
    data["is_manual_order"] = ~data["is_valid_amazon_de_order"]

    # Create order number
    data["No"] = (
        "AMSO-" 
        + pd.to_datetime(data["purchase-date"]).dt.strftime("%Y%m%d") 
        + "-" 
        + data["amazon-order-id"]
    )

    # Split data into valid and flagged orders
    valid_data = data[data["is_valid_amazon_de_order"] == True]
    flagged_data = data[data["is_manual_order"] == True]

    logging.info(f"Valid Amazon.de order lines: {len(valid_data)}")
    logging.info(f"Flagged/manual order lines: {len(flagged_data)}")

    return data, valid_data, flagged_data


def build_order_dfs(data: DataFrame) -> tuple[DataFrame, DataFrame]:
    logging.info("Building header and line DataFrames")

    header_df = pd.DataFrame()
    lines_df = pd.DataFrame()

    # Header mapping
    for am_col, bc_col in Mappings.salesOrderHeader.items():
        if am_col in data.columns:
            header_df[bc_col] = data[am_col]
    
    header_df["No"] = data["No"]
    header_df["Sell_to_Customer_No"] = data["Sell_to_Customer_No"]

    # Line mapping
    for am_col, bc_col in Mappings.salesOrderLine.items():
        if am_col in data.columns:
            lines_df[bc_col] = data[am_col]

    lines_df["Document_No"] = data["No"]
    lines_df["Unit_Price"] = data["Unit_Price"]

    logging.info(f"Building header and line DataFrames complete | lines: {len(lines_df)}")

    return header_df, lines_df


def mask_fields(df: DataFrame) -> DataFrame:
    data_mask = df.copy()

    mask_value = "*" * 10 
    for col in Mappings.mask_columns:
        if col in data_mask.columns:
            data_mask[col] = mask_value

    return data_mask


def transform(raw_data: dict) -> tuple[DataFrame, DataFrame, dict]:

    logging.info("Starting TRANSFORM step")

    # Exract raw data
    am_orders_df = extract_to_transform(raw_data)

    # 5 Prepare data
    data, valid_data, flagged_data = prepare_amazon_order(am_orders_df)

    # Build valid order header and line DataFrames
    header_df, lines_df = build_order_dfs(valid_data)

    # Build header and line dataframes from class objects
    sales_headers_df = build_sales_header_df(header_df)
    sales_lines_df = build_sales_line_df(lines_df)

    # Mask sensitive fields for output
    am_orders_df_masked = mask_fields(am_orders_df)
    sales_headers_df_masked = mask_fields(sales_headers_df)
    sales_lines_df_masked = mask_fields(sales_lines_df)
    flagged_data_masked = mask_fields(flagged_data)

    # Prepare load
    load_dfs = {
        "output": {
            "am_orders_df": am_orders_df,
            "data": data,
            "sales_headers_df": sales_headers_df,
            "sales_lines_df": sales_lines_df
        },
        "output_masked": {
            "am_orders_df_masked": am_orders_df_masked,
            "flagged_data_masked": flagged_data_masked,
            "sales_headers_df_masked": sales_headers_df_masked,
            "sales_lines_df_masked": sales_lines_df_masked
        }
    }

    
    logging.info("TRANSFORM step completed")

    return sales_headers_df, sales_lines_df, load_dfs