In the original setup, TXT files were imported into Excel and processed using Power Query and DAX.  
In this Python-based redesign, I’ve rebuilt the workflow as a modern ETL pipeline with a SQL staging layer and Python-driven transformations.  
The TXT files are manually consolidated and masked in an Excel sheet, then loaded into a SQL database as the staging environment.  
Python extracts the staged data, performs the necessary transformations, and produces the same reports as the original Excel solution.
