
def prepare_amazon_order():
    

    return



def calculate_unit_price():

    # DIVIDE( 'Amazon Order Files'[vat-exclusive-item-price]
	# 		+ 'Amazon Order Files'[shipping-price]
	# 		- 'Amazon Order Files'[shipping-tax] 
	# 		+ 'Amazon Order Files'[gift-wrap-price]
	# 		- 'Amazon Order Files'[gift-wrap-tax]
	# 		- 'Amazon Order Files'[item-promotion-discount]
	# 		- 'Amazon Order Files'[ship-promotion-discount]; 
	# 	'Amazon Order Files'[quantity];


    return




def customer_no_vat_cat(vat_percent, buyer_tax_id):
    if vat_percent is None and buyer_tax_id:
        return "CUS1025197"   # EU B2B zero-rated
    if vat_percent == 19:
        return "CUS1002096"   # DE domestic VAT
    return None



def valid_order():
    # df["is_valid_amazon_de_order"] = (
    # (df["is-amazon-invoiced"] == True)
    # & (df["order-status"] == "Shipped")
    # & (df["sales-channel"] == "Amazon.de")
    # & (df["VAT % (Calculated)"].isin([0, 19]))
    # & (df["Count Order lines"] == 1)
    # & (df["currency"] == "EUR")
    # & (~df["buyer-tax-registration-id"].str.contains(",", na=False))
    # & (df["Sell-To Customer No."].notna())
    # )

    # df["is_manual_order"] = ~df["is_valid_amazon_de_order"]


    return


def transform(raw_data):


    return raw_data



