from mlops.logger.logger import log
import pandas as pd
import numpy as np
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig: 
        raw_data_path: str=os.path.join("artifacts","raw_data.csv")
        train_data_path: str= os.path.join("artifacts","train_data.csv")
        test_data_path: str=os.path.join("artifacts","test_data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self): 
        try: 
            data=pd.read_csv("/Users/abishekkumaryadav/DataScience/Machine_learning/mlops_implementation/gemstone.csv")
            log.info(f"Data load sucessfully: {data.head()}")
            # os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_Data)), exist_ok=True)
            # data.to_csv(self.ingestion_config.raw_data)

            log.info(f"Performing train and test split of raw_data")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            train_data, test_data=train_test_split(data, test_size=0.30, random_state=42)

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            log.info(f"training data : {train_data.head(2)}")

            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            log.info(f"testing data : {test_data.head(2)}")

            log.info("Data Ingestion Completed")

            return {
                 self.ingestion_config.train_data_path,
                 self.ingestion_config.test_data_path
            }


        except Exception as e: 
            raise e
        

if __name__ == "__main__": 
     obj=DataIngestion()
     obj.initiate_data_ingestion()