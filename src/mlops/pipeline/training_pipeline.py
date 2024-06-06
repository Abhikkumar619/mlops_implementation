import os
import sys
from mlops.logger.logger import log
# from src.exception.exception import customexception
import pandas as pd

from mlops.components.data_ingestion import DataIngestion
from mlops.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer
# from src.components.model_evaluation import ModelEvaluation


obj=DataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()
log.info(f"From training pipeline Train_path: {train_data_path} and Test path: {test_data_path}")

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initiate_data_Transformation(train_path=train_data_path, test_path=test_data_path)



# model_trainer_obj=ModelTrainer()
# model_trainer_obj.initate_model_training(train_arr,test_arr)

# model_eval_obj = ModelEvaluation()
# model_eval_obj.initiate_model_evaluation(train_arr,test_arr)