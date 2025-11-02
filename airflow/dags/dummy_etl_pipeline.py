
""" Dummy ETL Pipeline"""

from datetime import datetime
from airflow.sdk import task, dag

# DAG Defination
@dag(
    dag_id = "Dummy-ETL-Pipeline",
    description = "Dummy ETL pipeline to execute Extract, Transform, Load Workflow",
    start_date = datetime(2025, 11, 2),
    schedule = None,
    catchup = False,
    tags = ["etl", "revenue-pipeline"]
)
def etl_dag():
    """
    ETL Pipeline
    """
    @task
    def extract_data(**context):
        print("Executing context date:", context["ds"])
        raw_records = [
            {"id": 1, "value": 10},
            {"id": 2, "value": 20},
            {"id": 3, "value": 30}
        ]
        return raw_records

    @task
    def transform_data(raw_data):
        """Takes raw data, calculates a total, and returns the result."""
        total_sum = sum(item['value'] for item in raw_data)
        return total_sum

    @task
    def load_data(final_result):
        """Loads the final result (the sum) to a destination (simulated print)."""
        print(f"Pipeline finished! Total value to load: {final_result}")

    raw_records = extract_data()
    total = transform_data(raw_data=raw_records)
    load_data(total)

etl_dag()
