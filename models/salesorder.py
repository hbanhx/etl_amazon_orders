from dataclasses import dataclass

from dataclasses import dataclass

@dataclass
class SalesOrderHeader:
    documentType: str
    number: str
    sellToCustomerNumber: str
    externalDocumentNumber: str
    orderDate: str
    postingDate: str
    vatRegistrationNo: str




    # @classmethod
    # def create_salesOrder(cls, row):
    #     return salesOrder = cls(
    #         documentType = "Order"
    #         number: str
    #         sellToCustomerNumber: str
    #         externalDocumentNumber: str
    #         orderDate: str
    #         postingDate: str
    #         vatRegistrationNo: str
    #     )