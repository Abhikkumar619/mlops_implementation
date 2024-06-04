import pandas as pd
import numpy as np
import os
import sys
from src.mlops.logger.logger import log
from dataclasses import dataclass
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler


@dataclass
class DataTransformation: 
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation: 
    def __init__(self):
        self.data_transformation_config=DataTransformation()

    
    def get_data_transformation(self): 
        try: 
            log.info("Data Transformation Started")
            categorical_col=['cut','color','clarity']
            numerical_col=['carat', 'depth', 'table', 'x', 'y', 'z']

            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            num_pipeline=Pipeline(
            steps=[
                ("imputer",SimpleImputer()),
                ("scaler",StandardScaler())])
            
            cat_pipeline=Pipeline(

            steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("ordinalencoder",OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories]))])
            
            preprocessor=ColumnTransformer([
                ("numerical_pipeline", num_pipeline, numerical_col ),
                ("categorical_pipeline",cat_pipeline, categorical_col)])
            

            return preprocessor


        except Exception as e: 
            raise e
        
    def initiate_data_Transformation(self, train_path, test_path): 
        train_data=pd.read_csv(train_path)
        test_data=pd.read_csv(test_path)

        preprocessor=self.get_data_transformation()

        target_column='price'
        drop_column='id'

        input_feature_train_df=train_data.drop(drop_column, axis=1)
        target_feature_train_df=train_data[target_column]

        input_feature_test_df=test_data.drop(drop_column, axis=1)
        target_feature_test_df=test_data[target_column]

        input_feature_train_arr=preprocessor.fit_transform(input_feature_train_df)
        input_feature_test_arr=preprocessor.fit_transform(input_feature_test_df)


        train_arr=np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
        test_arr=np.c_[input_feature_test_df, np.array(target_feature_test_df)]

        log.info(f"Training array after transformation: {train_arr[0:5]}")
        log.info(f"Testing array after transformation : {test_arr[0:4]}")





