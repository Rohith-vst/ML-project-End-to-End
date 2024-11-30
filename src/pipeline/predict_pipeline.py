import sys 
import pandas as pd
from src.exception import CustomException
from src.utils import load_object # to load pickle file

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features): # Here the model weights,preprocesser stored in artifacts is read using load_object defined in utils and returns the prediction.Predict will be called in app .py
        try:
            model_path = 'artifacts\model.pkl'
            preprocess_path  = 'artifacts/preprocessor.pkl'
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocess_path) 
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



# CustomData maps the data from front end (i.e is the input for prediction)to the model
class CustomData:
    def __init__( self,gender :str,
              race_ethnicity: int,
              parental_level_of_education ,
              lunch :str,
              test_preparation_course:str,
              reading_score: int,
              writing_score:int):
        

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

#mapping the data to form data frame
    def get_data_as_data_frame(self):
        try:
                custom_data_input_dict = {
                    "gender": [self.gender],
                    "race_ethnicity": [self.race_ethnicity],
                    "parental_level_of_education": [self.parental_level_of_education],
                    "lunch": [self.lunch],
                    "test_preparation_course": [self.test_preparation_course],
                    "reading_score": [self.reading_score],
                    "writing_score": [self.writing_score],
                }

                return pd.DataFrame(custom_data_input_dict)
        

        except Exception as e:
            raise CustomException(e, sys)