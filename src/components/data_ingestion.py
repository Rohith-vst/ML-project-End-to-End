import os
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #if you are only defining varaibles then we can use this decorator insted of using init
class DataIngestionConfig:
    '''This function helps in giving a customized input to the dataingestion 
     component where we can specify details like where can i store the train,test,raw data etc'''
    train_data_path :str=os.path.join('artifacts',"train.csv")
    test_data_path :str=os.path.join('artifacts',"test.csv")
    raw_data_path :str=os.path.join('artifacts',"raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self): # function to read the data from  the datasources
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') #we choose here from where to read the data ,We can use mangodb mysql etc
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #creating actual folders for the given paths

            df.to_csv(self.ingestion_config.raw_data_path,index = False,header= True)# saving raw data in csv to 

            logging.info("Train test split intitated")
            train_set,test_set =train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
            


if __name__ == "__main__":#if __name__ == "__main__": in Python is used to ensure that certain code is only executed when the script is run directly, and not when it is imported as a module in another scrip
    obj = DataIngestion()
    obj.initiate_data_ingestion() # python -m src.components.data_ingestion -- use this code to execute




