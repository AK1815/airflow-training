import sys
import airflow
from airflow import DAG, macros
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

with DAG(dag_id="templates_rendering", schedule_interval="@daily", default_args=default_args,tags=['basic_dags']) as dag:

    task1 = BashOperator(
            task_id="task1",
            bash_command="echo {{ds}}")

    task2 = BashOperator(
            task_id="task2",
            bash_command="echo {{var.value.DATACENTER}}")
 
    task3 = BashOperator(
            task_id="task3",
            bash_command="echo {{ ts_nodash }} - {{ macros.ds_format(ts_nodash, '%Y%m%dT%H%M%S', '%Y-%m-%d-%H-%M') }}")


    task4 = BashOperator(
            task_id="task4",
            bash_command="scripts/script.sh")

    task1 >> task2 >> task3 >> task4