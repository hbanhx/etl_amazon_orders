class Mappings:

    salesOrderHeader = {
        "amazon-order-id": "externalDocumentNumber",
        "Sell-To Customer No.": "sellToCustomerNumber",
        "purchase-date": "orderDate",
        "posting-date": "postingDate",
        "buyer-tax-registration-id": "vatRegistrationNo",
    }

    salesOrderLine = {
        "sku": "itemNo",
        "quantity": "quantity",
        "unit_price": "unitPrice",
        "location": "locationCode",
    }


    
    
    # salesOrder = {
    #     "Document Type No."
    #     "Sell-to Customer No."
    #     "Your Reference"
    #     "Order Date"
    #     "Posting Date"
    #     "VAT Registration No."
    #     "External Document No."
    # }

    # salesOrderLine = {
    #     "Document Type"
    #     "Document No."
    #     "Line No."
    #     "Type No."
    #     "Location Code"
    #     "Quantity"
    #     "Unit Price"
    # }