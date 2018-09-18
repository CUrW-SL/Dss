from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

mike11_dag = DAG('mike11_dag', default_args=default_args)

init_mike11 = BashOperator(
    task_id='init_mike11',
    bash_command='date',
    dag=mike11_dag)

run_mike11 = BashOperator(
    task_id='run_mike11',
    bash_command='sleep 5',
    retries=3,
    dag=mike11_dag)

upload_mike11 = BashOperator(
    task_id='upload_mike11',
    bash_command='sleep 5',
    retries=3,
    dag=mike11_dag)

extract_mike11 = BashOperator(
    task_id='extract_mike11',
    bash_command='date',
    dag=mike11_dag)

init_mike11 >> run_mike11 >> upload_mike11 >> extract_mike11