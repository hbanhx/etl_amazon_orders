class Mappings:
    # Map AM to BC table fields
    salesOrderHeader = {
        "amazon-order-id": "External_Document_No",
        "buyer-company-name": "Sell_to_Customer_Name",
        "purchase-date": "Order_Date",
        "last-updated-date": "Posting_Date",
        "buyer-tax-registration-id": "VAT_Registration_No",
        "currency": "Currency_Code"
    }
    # Map AM to BC table fields
    salesOrderLine = {
        "sku": "No",
        "quantity": "Quantity"
    }

    mask_columns = [
        "amazon-order-id",
        "buyer-company-name",
        "buyer-tax-registration-id",
        "Sell_to_Customer_No",
        "Sell_to_Customer_Name",
        "External_Document_No",
        "VAT_Registration_No"
    ]