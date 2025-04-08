## Used for generic Functionalities 

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')

def read_sql_db():
    
    
    logging.info("Reading SQL Database")
    
    try:
        logging.info("trying to read SQL Database")
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db            
        )
        logging.info("Connection Eastablished with :", mydb)
        df = pd.read_sql_query('Select * from Students', mydb)
        print(df.head())
        
        return df
    except Exception as ex:
        raise CustomException(ex)
