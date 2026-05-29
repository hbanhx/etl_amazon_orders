
def prepare_amazon_order():

    #  ["VAT % (Calculated)"]
    

    return



def calculate_unit_price(data):

    unit_price= (
        data[vat-exclusive-item-price]
        + data[shipping-price]
        - data[shipping-tax]
        + data[gift-wrap-price]
        - data[gift-wrap-tax]
        - data[item-promotion-discount]
        - data[ship-promotion-discount]
        ) / data[quantity]
            


    return data




def customer_no_vat_cat(vat_percent, buyer_tax_id):
    if vat_percent is None and buyer_tax_id:
        return "CUS1025197"   # EU B2B zero-rated
    if vat_percent == 19:
        return "CUS1002096"   # DE domestic VAT
    return None



def valid_order():
    # data["is_valid_amazon_de_order"] = (
    # (data["is-amazon-invoiced"] == True)
    # & (data["order-status"] == "Shipped")
    # & (data["sales-channel"] == "Amazon.de")
    # & (data["VAT % (Calculated)"].isin([0, 19]))
    # & (data["Count Order lines"] == 1)
    # & (data["currency"] == "EUR")
    # & (~data["buyer-tax-registration-id"].str.contains(",", na=False))
    # & (data["Sell-To Customer No."].notna())
    # )

    # data["is_manual_order"] = ~data["is_valid_amazon_de_order"]


    return


def transform(raw_data):


    return raw_data



