from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Python 함수 정의
def hello_world():
    print("Hello, World!")

# DAG 정의
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG(
    'simple_hello_world',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval='@daily',  # 매일 실행
)

# 작업 정의
hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=hello_world,
    dag=dag,
)

# 작업 순서 정의
hello_task
