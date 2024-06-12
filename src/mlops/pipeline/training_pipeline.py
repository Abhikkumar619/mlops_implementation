import os
import sys
from mlops.logger.logger import log
# from src.exception.exception import customexception
import pandas as pd

from mlops.components.data_ingestion import DataIngestion
from mlops.components.data_transformation import DataTransformation
from mlops.components.model_trainer import ModelTrainer
from mlops.components.model_evaluation import ModelEvaluation


class TrainingPipeline: 

    def start_data_ingestion(self): 
        try:
            obj=DataIngestion()
            train_data_path,test_data_path=obj.initiate_data_ingestion()
            log.info(f"From training pipeline Train_path: {train_data_path} and Test path: {test_data_path}")
            
            return train_data_path, test_data_path
        except Exception as e: 
            raise e
        
    def start_data_transformation(self, train_data_path, test_data_path):
        try: 
            data_transformation=DataTransformation()
            train_arr,test_arr=data_transformation.initiate_data_Transformation(train_path=train_data_path, test_path=test_data_path)
            return train_arr, test_arr
        except Exception as e: 
            raise e

    def start_model_training(self,train_arr, test_arr):
        try:
            model_trainer_obj=ModelTrainer()
            model_trainer_obj.initate_model_training(train_arr,test_arr)
 
            
        except Exception as e:
            raise e
    
    def model_evaluation(self, train_arr,test_arr): 
        try: 
            model_eval_obj = ModelEvaluation()
            model_eval_obj.initiate_model_evaluation(train_arr,test_arr)
        except Exception as e: 
            raise e
        
    def start_training(self):
        try: 
            train_data_path, test_data_path=self.start_data_ingestion()
            train_arr, test_arr=self.start_data_transformation(train_data_path, test_data_path)
            self.model_evaluation(train_arr, test_arr)
            self.start_model_training(train_arr, test_arr)
        
        except Exception as e:
            raise e






