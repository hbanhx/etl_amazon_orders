# ETL Amazon Orders Integration (Fake BC)

This pipeline replicates a real NAV RapidStart Excel import process.  
The workflow was rebuilt in Python and SQL and optimized using a one‑month sample:  
4,580 total Amazon orders processed, 4,127 auto‑integrated (≈90%), 453 flagged for manual review.


A Python ETL that:
1. Extracts Amazon order data from SQL Server
2. Transforms it into Business Central–style Sales Headers & Sales Lines
3. Loads the results into a Fake Business Central API, Excel files, and SQL Server

---

## Project Structure

    etl_amazon_orders/
    |
    ├── .gitignore
    ├── README.md
    |
    ├── etl/
    |   ├── main.py
    |   ├── extract/             # SQL extraction
    |   ├── transform/           # Transform logic
    |   ├── load/                # Load to API, SQL, Excel
    |   ├── config.yaml          [ignored]
    |   ├── output/              [ignored]  # Unmasked Excel output
    |   ├── output_masked/       # Masked Excel output
    |   ├── application/         # Fake BC API client
    |   ├── builders/            # Build SalesHeader / SalesLine objects
    |   ├── data/                [ignored]  # Raw Excel inputs
    |   ├── logs/                [ignored]  # ETL logs
    |   ├── mappings/            # Amazon → BC field mappings
    |   └── models/              # SalesHeader / SalesLine dataclasses
    |
    └── fake_business_central_fastapi/
        └── fake_bc_api.py       # Fake BC FastAPI service


---

## Pipeline Overview

**Extract**
- Connects to SQL Server using SQLAlchemy
- Loads queries from `etl/config.yaml`
- Returns raw Amazon order data

**Transform**
- Computes unit price & VAT
- Assigns customer numbers
- Flags valid vs. manual orders
- Maps Amazon fields → BC fields
- Builds SalesHeader & SalesLine objects
- Masks sensitive fields
- Prepares output dicts for Excel export

**Load**
- Sends orders & lines to Fake BC API
- Writes Excel files to `etl/output/` and `etl/output_masked/`
- Writes SQL tables (`salesHeader`, `salesLine`) to GS_DB

---

## Running the Pipeline

Start the Fake BC API:

uvicorn fake_business_central_fastapi.fake_bc_api:app --host 127.0.0.1 --port 8000

Run the ETL:

.\.venv\Scripts\activate
python etl/main.py

---

## Requirements

- Python 3.10+
- SQL Server + ODBC Driver 17
- FastAPI, SQLAlchemy, Pandas, Uvicorn
