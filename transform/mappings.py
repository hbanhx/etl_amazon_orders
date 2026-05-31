class Mappings:
    # Map AM to BC fields
    salesOrderHeader = {
        "amazon-order-id": "externalDocumentNumber",
        # "": "sellToCustomerNumber",
        "buyer-company-name": "customerName",
        "purchase-date": "orderDate",
        "posting-date": "postingDate",
        "buyer-tax-registration-id": "vatRegistrationNo",
    }

    salesOrderLine = {
        "sku": "itemNo",
        "quantity": "quantity",
        "unit_price": "unitPrice",
        "location": "locationCode"
    }