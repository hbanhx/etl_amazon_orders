from typing import Any
import requests

BASE_URL = "http://127.0.0.1:8000"
COMPANY_ID = "fake_company"


def post_sales_order_to_bc(header_dict: dict[str, Any]) -> dict[str, Any]:
    # Sends a sales order header to the fake BC API.
    # Returns the created order (with id + documentLines).

    url = f"{BASE_URL}/fake_bc/companies/{COMPANY_ID}/salesOrders"
    response = requests.post(url, json=header_dict)
    response.raise_for_status()
    return response.json()


def post_sales_order_line_to_bc(order_id: str, line_dict: dict[str, Any]) -> dict[str, Any]:
    # Sends a sales order line to the fake BC API.
    # Returns the created line.

    url = f"{BASE_URL}/fake_bc/companies/{COMPANY_ID}/salesOrders/{order_id}/salesOrderLines"
    response = requests.post(url, json=line_dict)
    response.raise_for_status()
    return response.json()