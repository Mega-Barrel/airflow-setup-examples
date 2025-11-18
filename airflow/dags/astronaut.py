
"""
Airflow Dag to return list of Astronauts currently in Space and prints
each Astronauts name and flying craft.
"""

from datetime import datetime, timedelta

from utils.get_astronaut import get_astronauts
from utils.print_astronaut import print_astronauts

from airflow.models.dag import DAG
from airflow.providers.standard.operators.python import PythonOperator

# DAG Definition
with DAG(
    dag_id = "astronauts-daily-data",
    description = "Airflow DAG to pull daily data of Astronauts who are currently in space",
    start_date = datetime(2025, 11, 18),
    schedule = "@daily",
    default_args = {
        "owner": "Saurabh Joshi",
        "retries": 1,
        "retry_delay": timedelta(seconds = 20),
        "email_on_failure": False
    },
    tags = [
        "Astronauts", "ISS-data-feed"
    ]
) as dag:
    # Task 1: Call the API to pull real time Astronauts data
    get_astronauts_task = PythonOperator(
        task_id="get_astronauts",
        python_callable=get_astronauts,
    )

    # Task 2: Print the data from X-Com
    print_astronauts_task = PythonOperator(
        task_id = 'print_astronauts',
        python_callable = print_astronauts,
    )

    get_astronauts_task >> print_astronauts_task
