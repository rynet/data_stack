from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.custom import Custom
from diagrams.onprem.database import MSSQL, PostgreSQL
from diagrams.generic.place import Datacenter
from diagrams.aws.analytics import Kinesis
from diagrams.aws.storage import S3
from diagrams.saas.analytics import Snowflake
from diagrams.onprem.analytics import Dbt, PowerBI
from diagrams.programming.language import Python
from diagrams.saas.chat import Slack


with Diagram("Data Tech Stack", direction="LR"):
    with Cluster("Source Data"):
        # Marketing & Ecom: Google Analytics
        # Behavioural/Product Usage/Events: Snowplow
        # Relational DB: Microsoft SQL
        # NoSQL/JSON: Postgress
        # Misc third parties

        with Cluster("Databases"):
            databases = [PostgreSQL("NoSQL:\n Postgres"), 
                    MSSQL("Relational DB:\n MSSQL")
            ]

        with Cluster("Behavioural/Events"):
            snowplow = Custom("Snowplow", ".\\img\\snowplow.png")
            kinesis = Kinesis("Kinesis")
            snowplow >> kinesis
        #ga = BigQuery("Site Analytics: GA/BigQuery")
        with Cluster("Site Analytics"):
            ga = Custom("Google Analytics", ".\\img\\ga.png")
            bigquery = BigQuery("BigQuery")
            ga >> bigquery
    
    with Cluster("ELT & Orchestration"):
        matillion = Custom("ELt: Matillion", ".\\img\\matillion.png")
        dbt = Dbt("elT: Dbt")

    with Cluster("Storage"):
        s3 = S3("Lake/Storage:\n S3")
        snowflake = Snowflake("Warehouse:\n Snowflake")
    
    with Cluster("Consumption"):
        powerbi = PowerBI("Dashbaords: PowerBI")
        python = Python("Programmatic: Python")
        colab = Custom("Notebook: Colab", ".\\img\\colab.png")
        slack = Slack("Alerts: Slack")

    # data sources via matillion
    databases >> matillion >> dbt >> snowflake
    # data sources written directly to lake/S3
    [kinesis, bigquery] >> s3 >> snowflake

    # Data use cases, from snowflake
    snowflake >> powerbi
    snowflake >> python
    snowflake >> colab
    snowflake >> slack
    