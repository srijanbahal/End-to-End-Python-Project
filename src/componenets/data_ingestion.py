## MySQL ---> Train-test-split ---> Dataset

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from src.utils import read_sql_db
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')  


class DataIngestion: 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    #01 Reading from MySQL Database
    def initiate_data_ingestion(self):
        try: 
            ## Reading the dats from mysql
            
            
            # notebooks\Data\raw.csv
            # df = read_sql_db()
            df = pd.read_csv(os.path.join('notebooks/Data', 'raw.csv'))
            logging.info("Reading From mysql database")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)
            
            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header = True)
            
            logging.info("Data Ingestion is Completed")
          
            return (
              self.ingestion_config.train_data_path,
              self.ingestion_config.test_data_path
            )
            
            
        except Exception as e:
            raise CustomException(e,sys)