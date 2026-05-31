import pandas as pd


def extract_to_transform(raw_data):
    return raw_data["am_orders"]

def prepare_amazon_order(am_order_data):

    data = am_order_data.copy()
    
    data["unit_price"]= (
        data["vat-exclusive-item-price"]
        + data["shipping-price"]
        - data["shipping-tax"]
        + data["gift-wrap-price"]
        - data["gift-wrap-tax"]
        - data["item-promotion-discount"]
        - data["ship-promotion-discount"]
        ) 
    
    data["vat_pct"] = round(data["item-tax"] / data["unit_price"].where(data["quantity"] != 0), 2) #.astype(float)

    data["Sell-To Customer No."] = None
    data.loc[(data["vat_pct"].isna() | data["vat_pct"] == 0) & data["buyer-tax-registration-id"].notna(), "Sell-To Customer No."] = "CUS1025197"
    data.loc[data["vat_pct"] == 0.19, "Sell-To Customer No."] = "CUS1002096"


    data["is_valid_amazon_de_order"] = (
        (data["is-amazon-invoiced"] == True)
        & (data["order-status"] == "Shipped")
        & (data["sales-channel"] == "Amazon.de")
        & (data["vat_pct"].isin([0, 0.19]))
        & (data["currency"] == "EUR")
        & (~data["buyer-tax-registration-id"].str.contains(",", na=False))
        & (data["Sell-To Customer No."].notna())
        )

    data["is_manual_order"] = ~data["is_valid_amazon_de_order"]


    return data


def create_sales_order(am_order_data):
    # excel versino create the header, create an id (from am numberseries), store in am_dataframe

    order_header = am_order_data.groupby(am_order_data["amazon-order-id"])
    print(type(order_header))
    print(order_header)
    for index, row in order_header:
        print(index, row)

    # return sales_order


def create_sales_order_lines(am_order_data):
    # excel version: group.by am order Id, get the sales order header ID, create the lines store in lines_dataframe, load header_df to a sheet1, load lines to sheet2
    for index, row in am_order_data.iterows():
        pass
        
    # return sales_order_lines


def transform(raw_data):


    am_order_data = extract_to_transform(raw_data)

    am_order_data = prepare_amazon_order(am_order_data)
    print(type(am_order_data))

    sales_order_header = create_sales_order(am_order_data)
    # sales_order_lines = create_sales_order_lines()


    return am_order_data



