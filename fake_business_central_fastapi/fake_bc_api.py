from fastapi import FastAPI
import uuid

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello fake bc"}


# in memory, not in db
SALESORDERS = {}
SALESLINES = {}

@app.post("/fake_bc/companies/{company_id}/salesOrders")
def create_order(company_id: str, body: dict):
    order_id = str(uuid.uuid4())

    order = {
        "id": order_id,
        "company_id": company_id,
        **body,
        "documentLines": []
    }

    SALESORDERS[order_id] = order
    return order


@app.post("/fake_bc/companies/{company_id}/salesOrders/{order_id}/salesOrderLines")
def create_line(company_id: str, order_id: str, body: dict):
    line_id = str(uuid.uuid4())

    line = {
        "id": line_id,
        "order_id": order_id,
        **body
    }

    SALESLINES[line_id] = line
    SALESORDERS[order_id]["documentLines"].append(line)

    return line


@app.get("/fake_bc/companies/{company_id}/salesOrders")
def get_orders(company_id: str):
    orders = []
    for order in SALESORDERS.values():
        if order["company_id"] == company_id:
            orders.append(order)
    return orders

@app.get("/fake_bc/companies/{company_id}/salesOrders/{order_id}")
def get_order(company_id: str, order_id: str):
    for order in SALESORDERS.values():
        if order["company_id"] == company_id and order["id"] == order_id:
            return order
# fake_company
# f290ca5b-b424-4e41-a743-9d44015b5852