
FROM apache/airflow:3.1.1

USER root

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean
USER airflow
