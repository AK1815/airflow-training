import sys
import airflow
from airflow.models import Variable
from airflow import DAG, macros
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.decorators import task

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

def add_fn(x):
    return x 

def multiply_fn(x,y):
    return x * y


with DAG(dag_id="python_operator", schedule_interval="@daily", default_args=default_args,tags=['assignment']) as dag:

    #TODO: Add a python operator task to call "add_fn" function defined above in your pipeline
     t1 = PythonOperator(
                 task_id="Ak_Task",
                 python_callable=add_fn,
                 op_kwargs= {'x':4}
                 dag=dag
                 )

    #TODO: Add a python operator task to call "multiply_fn" function defined above in your pipeline


    #TODO: Add dependencies as shown in assignment
     t1            
