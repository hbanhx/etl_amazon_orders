from dataclasses import dataclass

# https://learn.microsoft.com/en-us/dynamics365/business-central/application/base-application/table/microsoft.sales.document.sales-line

@dataclass
class SalesLine:
    Document_Type: str
    Document_No: str
    Type: str
    Line_No: int
    No: str
    Location_Code: str
    Quantity: float
    Unit_Price: float


    @classmethod
    def from_row(cls, line_no, row):
        SalesLine = cls(
            Document_Type = "Order",
            Document_No = row["Document_No"],
            Type = "Item",
            Line_No = line_no,
            No = row["No"],
            Location_Code = "AMAZON.DE",
            Quantity = row["Quantity"],
            Unit_Price = row["Unit_Price"]
        )

        return SalesLine