import os
import sys
import pandas as pd
from src.mlops.logger.logger import log
from src.mlops.utils.common import load_object


class PredictPipeline: 
    def __init__(self):
        pass

    def predict(self, fearures): 
        try: 
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            scaled_features=preprocessor.transform(fearures)
            pred=model.predict(scaled_features)

            return pred

        except Exception as e: 
            raise e
        

class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity
            
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
                }
            df = pd.DataFrame(custom_data_input_dict)
            log.info('Dataframe Gathered')
            return df
        except Exception as e:
            log.info('Exception Occured in prediction pipeline')
            raise e