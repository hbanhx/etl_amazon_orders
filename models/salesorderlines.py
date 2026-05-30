from dataclasses import dataclass

@dataclass
class salesOrderLine:

    "Document Type"
    "Document No."
    "Line No."
    "Type No."
    "Location Code"
    "Quantity"
    "Unit Price"


    def create_sales_order_lines(sol, row):
        pass