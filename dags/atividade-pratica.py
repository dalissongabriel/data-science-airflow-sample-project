from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

def log_message():
    print("Cloud computing - Desenvolvimento em Cloud Aplicada ...")

def run_query():
    hook = PostgresHook(postgres_conn_id="postgres_default")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();") 
    result = cursor.fetchone()
    print(f"Resultado da consulta: {result}")

def choose_branch(**kwargs):
    return "executar_a" if datetime.now().minute % 2 == 0 else "executar_b"

def process_task_a():
    print("O comando A foi executado")

def process_task_b():
    print("O comando B foi executado")

default_args = {
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="alisson_dag",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="DAG complexa com múltiplos operadores, XCom e Branching"
) as dag:

    start = PythonOperator(
        task_id="log_message",
        python_callable=log_message
    )

    list_files = BashOperator(
        task_id="list_files",
        bash_command="ls -la"
    )

    query = PythonOperator(
        task_id="query_postgres",
        python_callable=run_query
    )

    branch = BranchPythonOperator(
        task_id="branch_task",
        python_callable=choose_branch,
        provide_context=True
    )

    executar_a = PythonOperator(
        task_id="executar_a",
        python_callable=process_task_a
    )

    executar_b = PythonOperator(
        task_id="executar_b",
        python_callable=process_task_b
    )

    fim = EmptyOperator(task_id="fim")

    start >> list_files >> query >> branch
    branch >> executar_a >> fim
    branch >> executar_b >> fim