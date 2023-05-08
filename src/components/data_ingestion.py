import os
import sys
import pandas as pd
from exception import CustomException
from logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #use only when you defining variables
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")
    
class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def inetiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("read student data from csv file")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)
            
            logging.info("Train and test split inetiated")
            train_set,test_set = train_test_split(df, test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index = False, header = True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index =False,header =True)
            
            logging.info("Ingestion the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
            pass
        except Exception as e:
            raise CustomException(e,sys)        
        
        
        
if __name__ == "__main__":
    obj = DataIngestion
    train_data,test_data = obj.inetiate_data_ingestion()        