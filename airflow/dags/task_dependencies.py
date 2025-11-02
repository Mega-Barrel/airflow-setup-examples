
""" Code for Python Task Dependencies"""

from datetime import datetime

from airflow.models.dag import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id = "example_dependencies",
    start_date=datetime(2023, 1, 1)
) as dag:
    start_task = EmptyOperator(task_id="start_task")

    middle_task_a = EmptyOperator(task_id="middle_task_a")
    middle_task_b = EmptyOperator(task_id="middle_task_b")

    middle_task = EmptyOperator(task_id = "main_middle_task")

    sleep_task_a = BashOperator(task_id = "sleep_a", bash_command="sleep 5")
    sleep_task_b = BashOperator(task_id = "sleep_b", bash_command="sleep 10")

    end_task = EmptyOperator(task_id="end_task")

    start_task >> [middle_task_a, middle_task_b]
    [middle_task_a, middle_task_b] >> middle_task
    middle_task >> [sleep_task_a, sleep_task_b]
    [sleep_task_a, sleep_task_b] >> end_task
