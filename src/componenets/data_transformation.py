## Takes Data from train-test Split one ---> Feature Engineering ---> pkl file

import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    
    

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        '''
        This Function is Responsible for handling Data Transformation
        '''
        # df = pd.read_csv('artifacts\raw.csv')
        
        try:
            # numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']
            # categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']
            numerical_features = ["writing_score", "reading_score"]
    
            categorical_features = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
        
            
            num_pipeline = Pipeline(steps = [
                ("imputer", SimpleImputer(strategy = 'median')),
                ('scaler', StandardScaler())
            ])
            cat_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])
            logging.info(f"Categorical Columns : {categorical_features}")
            logging.info(f"Numercial Columns : {numerical_features}")
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipline", num_pipeline, numerical_features),
                    ("cat_pipline", cat_pipeline, categorical_features)
                ]
            )
            return preprocessor
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Reading the train and test file")
            
            preprocessing_obj = self.get_data_transformer_object()
            
            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]
            
            # Dividing the Dataset into independent (X) and Dependent features(y)
            input_features_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            # Now for the test DF
            input_features_test_df = test_df.drop(columns=[target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info("Applying preprocessing On the train and test set")
            
            input_features_train_df= preprocessing_obj.fit_transform(input_features_train_df)
            input_features_test_df= preprocessing_obj.transform(input_features_test_df)
            

            train_arr = np.c_[
                input_features_train_df, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_features_test_df, np.array(target_feature_test_df)
            ]
            
            logging.info(f"Saved Preprocessing object")
            
            
            # Now Saving the file
            
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj  = preprocessing_obj
            )
            
            return (
                
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        
        
        
        
        
        
        
        
        
        
        except Exception as e:
            raise CustomException(e, sys)