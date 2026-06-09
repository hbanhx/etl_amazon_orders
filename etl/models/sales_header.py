import pandas as pd
from dataclasses import dataclass
# https://learn.microsoft.com/en-us/dynamics365/business-central/application/base-application/table/microsoft.sales.document.sales-header


@dataclass
class SalesHeader:
    Document_Type: str #BC - Order 
    No: str #BC
    Sell_to_Customer_No: str #BC
    Sell_to_Customer_Name: str
    External_Document_No: str
    Order_Date: str
    Posting_Date: str
    VAT_Registration_No: str
    Currency_Code: str

    @classmethod
    def from_row(cls, row):

        SalesHeader = cls(
            Document_Type = "Order",
            No = row["No"],
            Sell_to_Customer_No = row["Sell_to_Customer_No"],
            Sell_to_Customer_Name = row["Sell_to_Customer_Name"],
            External_Document_No = row["External_Document_No"],
            Order_Date = pd.to_datetime(row["Order_Date"]).strftime("%Y-%m-%d"),
            Posting_Date = pd.to_datetime(row["Posting_Date"]).strftime("%Y-%m-%d"),
            VAT_Registration_No = row["VAT_Registration_No"],
            Currency_Code = row["Currency_Code"]
        )

        return SalesHeader