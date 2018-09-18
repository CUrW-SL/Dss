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

wrf0_dag = DAG('wrf0_dag', default_args=default_args)

init_wrf0 = BashOperator(
    task_id='init_wrf0',
    bash_command='date',
    dag=wrf0_dag)

run_wrf0 = BashOperator(
    task_id='run_wrf0',
    bash_command='sleep 5',
    retries=3,
    dag=wrf0_dag)

upload_wrf0 = BashOperator(
    task_id='upload_wrf0',
    bash_command='sleep 5',
    retries=3,
    dag=wrf0_dag)

extract_wrf0 = BashOperator(
    task_id='extract_wrf0',
    bash_command='date',
    dag=wrf0_dag)

init_wrf0 >> run_wrf0 >> upload_wrf0 >> extract_wrf0

wrf1_dag = DAG('wrf1_dag', default_args=default_args)

init_wrf1 = BashOperator(
    task_id='init_wrf1',
    bash_command='date',
    dag=wrf1_dag)

run_wrf1 = BashOperator(
    task_id='run_wrf1',
    bash_command='sleep 5',
    retries=3,
    dag=wrf1_dag)

upload_wrf1 = BashOperator(
    task_id='upload_wrf1',
    bash_command='sleep 5',
    retries=3,
    dag=wrf1_dag)

extract_wrf1 = BashOperator(
    task_id='extract_wrf1',
    bash_command='date',
    dag=wrf1_dag)

init_wrf1 >> run_wrf1 >> upload_wrf1 >> extract_wrf1

wrf2_dag = DAG('wrf2_dag', default_args=default_args)

init_wrf2 = BashOperator(
    task_id='init_wrf2',
    bash_command='date',
    dag=wrf2_dag)

run_wrf2 = BashOperator(
    task_id='run_wrf2',
    bash_command='sleep 5',
    retries=3,
    dag=wrf2_dag)

upload_wrf2 = BashOperator(
    task_id='upload_wrf2',
    bash_command='sleep 5',
    retries=3,
    dag=wrf2_dag)

extract_wrf2 = BashOperator(
    task_id='extract_wrf2',
    bash_command='date',
    dag=wrf2_dag)

init_wrf2 >> run_wrf2 >> upload_wrf2 >> extract_wrf2