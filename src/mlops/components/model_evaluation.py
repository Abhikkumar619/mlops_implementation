import os
import sys
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from mlops.logger.logger import log
from mlops.utils.common import load_object
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import dagshub


class ModelEvaluation: 
    def __init__(self): 
        pass

    def eval_metrices(self, actual, pred): 
        rmse=np.sqrt(mean_squared_error(actual, pred))
        mae=mean_absolute_error(actual, pred)
        r2=r2_score(actual, pred)
        return rmse, mae, r2
    

    def initiate_model_evaluation(self, train_arr, test_arr):
        try: 
            log.info(f"Model evaluation start.")
            X_test,y_test=(test_arr[:,:-1], test_arr[:,-1])

            model_path=os.path.join("artifacts","model.pkl")
            model=load_object(model_path)

            dagshub.init(repo_owner='Abhikkumar619', repo_name='mlops_implementation', mlflow=True)

            mlflow.set_registry_uri("https://dagshub.com/Abhikkumar619/mlops_implementation.mlflow")
            tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme
            print(tracking_url_type_store)


            with mlflow.start_run():
                prediction=model.predict(X_test)

                (rmse, mae, r2)=self.eval_metrices(y_test, prediction)

                mlflow.log_metric("rmse",rmse)
                mlflow.log_metric("mae",mae)
                mlflow.log_metric("r2",r2)

                if tracking_url_type_store !='file': 
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                else: 
                    mlflow.sklearn.log_model(model, "model")
            
        except Exception as e: 
            raise e

