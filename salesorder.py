from dataclasses import dataclass

@dataclass
class salesOrder:

    "Document Type" 
    "No."
    "Sell-to Customer No."
    "Your Reference"
    "Order Date"
    "Posting Date"
    "VAT Registration No."
    "External Document No."


@dataclass
class salesOrderLine:

    "Document Type"
    "Document No."
    "Line No."
    "Type No."
    "Location Code"
    "Quantity"
    "Unit Price"
