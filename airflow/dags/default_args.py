
""" Code for Passing Default arguments to DAG"""

from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.providers.standard.operators.python import PythonOperator

args = {
    'owner': 'Saurabh Joshi',
    'retries': 2,
    'retry_delay': timedelta(seconds=10),
    'email_on_failure': False,
}

def failing_function():
    """ Method to raise ValueError Exception"""
    raise ValueError("This task is designed to fail!")

with DAG(
    dag_id = "default-agrs-dag",
    default_args = args,
    description = "This DAG runs with default arguments passed to it.",
    start_date = datetime(2025, 11, 3),
    tags = [
        "default-dag",
        "default-args"
    ]
) as dag:
    fail_task = PythonOperator(
        task_id='fail_task',
        python_callable=failing_function,
    )

