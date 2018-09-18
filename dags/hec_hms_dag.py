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

hec_hms0_dag = DAG('hec_hms0_dag', default_args=default_args)

init_hec_single = BashOperator(
    task_id='init_hec_single',
    bash_command='date',
    dag=hec_hms0_dag)

run_hec_single = BashOperator(
    task_id='run_hec_single',
    bash_command='sleep 5',
    retries=3,
    dag=hec_hms0_dag)

upload_hec_single = BashOperator(
    task_id='upload_hec_single',
    bash_command='sleep 5',
    retries=3,
    dag=hec_hms0_dag)

extract_hec_single = BashOperator(
    task_id='extract_hec_single',
    bash_command='date',
    dag=hec_hms0_dag)

init_hec_single >> run_hec_single >> upload_hec_single >> extract_hec_single

hec_hms1_dag = DAG('hec_hms1_dag', default_args=default_args)

init_hec_distributed = BashOperator(
    task_id='init_hec_distributed',
    bash_command='date',
    dag=hec_hms1_dag)

run_hec_distributed = BashOperator(
    task_id='run_hec_distributed',
    bash_command='sleep 5',
    retries=3,
    dag=hec_hms1_dag)

upload_hec_distributed = BashOperator(
    task_id='upload_hec_distributed',
    bash_command='sleep 5',
    retries=3,
    dag=hec_hms1_dag)

extract_hec_distributed = BashOperator(
    task_id='extract_hec_distributed',
    bash_command='date',
    dag=hec_hms1_dag)

init_hec_distributed >> run_hec_distributed >> upload_hec_distributed >> extract_hec_distributed