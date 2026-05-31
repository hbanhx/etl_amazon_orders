from dataclasses import dataclass

@dataclass
class SalesOrderLine:
    documentType: str
    documentNumber: str
    lineNo: int
    itemNo: str
    locationCode: str
    quantity: float
    unitPrice: float



    def create_sales_order_lines(cls, row):
        pass