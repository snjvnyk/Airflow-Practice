from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'start_date': datetime(2023, 3, 16)
}

dag = DAG(
    'sample_dag',
    default_args=default_args,
    schedule_interval=None,
)

task1 = BashOperator(
    task_id='task1',
    bash_command='echo "task1"',
    dag=dag,
)

def print_current_date():
    print(datetime.now())

task2 = PythonOperator(
    task_id='task2',
    python_callable=print_current_date,
    dag=dag,
)

task3 = DummyOperator(
    task_id='task3',
    dag=dag,
)
