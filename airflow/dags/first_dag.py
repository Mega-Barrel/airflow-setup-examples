""" Dag init """

from __future__ import annotations

from airflow.models.dag import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

# Define the DAG arguments
with DAG(
    dag_id = "test_simple_sequential_dag",
    schedule = None,
    catchup = False,
    tags = ["testing", "simple"],
) as dag:
    # 1. Define start task
    start_task = EmptyOperator(task_id="start_process")

    # 2. Define a simple Bash task
    bash_task = BashOperator(
        task_id="print_hello",
        bash_command='echo "Hello Airflow"',
    )

    # 3. Define another empty task for completion
    end_task = EmptyOperator(task_id="end_process")

    # Set dependencies
    start_task >> bash_task >> end_task
