from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add the path to the modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'stock_pipeline'))

from fetch_data import fetch_stock_data
from prepare_data import clean_data
from insert_data import insert_into_mysql

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='stock_data_pipeline',
    default_args=default_args,
    description='Pipeline to fetch, clean, and load stock data into Azure MySQL',
    schedule_interval=None,  # No automatic schedule
    catchup=False
) as dag:

    fetch = PythonOperator(
        task_id='fetch_stock_data',
        python_callable=fetch_stock_data
    )

    clean = PythonOperator(
        task_id='prepare_data',
        python_callable=clean_data
    )

    insert = PythonOperator(
        task_id='insert_into_mysql',
        python_callable=insert_into_mysql
    )

    fetch >> clean >> insert
