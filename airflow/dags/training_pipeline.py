from airflow import DAG
from airflow import PythonOperator
from src.mlops.pipeline.training_pipeline import TrainingPipeline
import datetime
from src.mlops.logger.logger import log
import numpy as np
training_pipeline=TrainingPipeline()


with DAG(
    "gamestone_training_pipeline",
    default_args={"retries":2},
    description="It is my training pipeline",
    schedule="@weekly",
    start_date=datetime.datetime(2024, 1, 17, tz="UTC"),
    catchup=False,
    tages=["machine_learning","classfication","gemestone"],
) as dag:
    
    dag.doc_md=__doc__

    def data_ingestion(**kwargs):
        ti=kwargs["ti"]
        train_data_path, test_data_path=training_pipeline.start_data_ingestion()
        ti.xcom_push("data_ingestion_artifacts",{"train_data_path": train_data_path, "test_data_path":test_data_path})

    def data_transformations(**kwargs):
        ti=kwargs["ti"]
        data_ingestion_artifact=ti.xcom_pull(task_ids="data_ingestion",key="data_ingestion_artifact")
        log.info(f"From ariflow data transformation:{data_ingestion_artifact}")
        train_arr, test_arr=training_pipeline.start_data_transformation(data_ingestion_artifact["train_data_path"], data_ingestion_artifact["test_data_path"])
        train_arr=train_arr.tolist()
        test_arr=test_arr.tolist()
        ti.xcom_push("data transformation_artifact", {"train_arr": train_arr, "test_arr": test_arr})

    def model_trainer(**kwargs):
        ti=kwargs["ti"]
        data_transformations_artifact= ti.xcom_pull(task_ids="data_transformation", key="data_transformations_artifact")
        train_arr=np.array(data_transformations_artifact["train_arr"])
        test_arr=np.array(data_transformations_artifact["test_arr"])
        training_pipeline.start_model_training(train_arr, test_arr)



    data_ingestion_task=PythonOperator(
        task_id="data_ingestion",
        python_callable=data_ingestion
    )

    data_transfrom_task=PythonOperator(
        task_id="data_transformation",
        python_callable=data_transformations,
    )

    model_trainer_task=PythonOperator(
        task_id="model_trainer",
        python_callable=model_trainer,
    )

    data_ingestion_task >> data_transfrom_task >> model_trainer_task
        
    
