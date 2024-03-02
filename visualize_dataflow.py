from diagrams import Diagram, Node
from diagrams.saas.analytics import Snowflake
from diagrams.onprem.analytics import Dbt, PowerBI
from diagrams.custom import Custom
from diagrams.onprem.analytics import PowerBI

DB_TABLE_IMG = ".\\img\\db_table.png"

with Diagram("Data Flow"):
    dbt = Dbt("DBT")
    snowflake = Snowflake("Snowflake")
    tbl_raw = Custom("Table: Raw Data", DB_TABLE_IMG)
    tbl_preprocess = Custom("Table: Pre-Process", DB_TABLE_IMG)
    tbl_staging = Custom("Table: Staging", DB_TABLE_IMG)
    tbl_analysis = Custom("Table: Analysis Tables", DB_TABLE_IMG)
    end_users = PowerBI("End Users")

    dbt >> snowflake >> tbl_raw >> tbl_preprocess >> tbl_staging >> tbl_analysis >> end_users
