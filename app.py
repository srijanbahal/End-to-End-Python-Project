from src.logger import logging
from src.exception import CustomException
from src.componenets.data_ingestion import DataIngestion
from src.componenets.data_ingestion import DataIngestionConfig
from src.componenets.data_transformation import DataTransformationConfig, DataTransformation
from src.componenets.model_trainer import ModelTrainerConfig,ModelTrainer
import sys

if __name__ == "__main__":
    logging.info("The Execution has Started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        
        
        # data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        train_arr,test_arr,_= data_transformation.initiate_data_transformation(train_path,test_path)

        ## Model Training

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    
    