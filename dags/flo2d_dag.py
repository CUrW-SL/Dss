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

flo2d0_dag = DAG('flo2d0_dag', default_args=default_args)

init_flo2d_250 = BashOperator(
    task_id='init_flo2d_250',
    bash_command='date',
    dag=flo2d0_dag)

run_flo2d_250 = BashOperator(
    task_id='run_flo2d_250',
    bash_command='sleep 5',
    retries=3,
    dag=flo2d0_dag)

upload_flo2d_250 = BashOperator(
    task_id='upload_flo2d_250',
    bash_command='sleep 5',
    retries=3,
    dag=flo2d0_dag)

extract_flo2d_250 = BashOperator(
    task_id='extract_flo2d_250',
    bash_command='date',
    dag=flo2d0_dag)

init_flo2d_250 >> run_flo2d_250 >> upload_flo2d_250 >> extract_flo2d_250

flo2d1_dag = DAG('flo2d1_dag', default_args=default_args)

init_flo2d_150 = BashOperator(
    task_id='init_flo2d_150',
    bash_command='date',
    dag=flo2d1_dag)

run_flo2d_150 = BashOperator(
    task_id='run_flo2d_150',
    bash_command='sleep 5',
    retries=3,
    dag=flo2d1_dag)

upload_flo2d_150 = BashOperator(
    task_id='upload_flo2d_150',
    bash_command='sleep 5',
    retries=3,
    dag=flo2d1_dag)

extract_flo2d_150 = BashOperator(
    task_id='extract_flo2d_150',
    bash_command='date',
    dag=flo2d1_dag)

init_flo2d_150 >> run_flo2d_150 >> upload_flo2d_150 >> extract_flo2d_150

flo2d2_dag = DAG('flo2d2_dag', default_args=default_args)

init_flo2d_30 = BashOperator(
    task_id='init_flo2d_30',
    bash_command='date',
    dag=flo2d2_dag)

run_flo2d_30 = BashOperator(
    task_id='run_flo2d_30',
    bash_command='sleep 5',
    retries=3,
    dag=flo2d2_dag)

upload_flo2d_30 = BashOperator(
    task_id='upload_flo2d_30',
    bash_command='sleep 5',
    retries=3,
    dag=flo2d2_dag)

extract_flo2d_30 = BashOperator(
    task_id='extract_flo2d_30',
    bash_command='date',
    dag=flo2d2_dag)

init_flo2d_30 >> run_flo2d_30 >> upload_flo2d_30 >> extract_flo2d_30