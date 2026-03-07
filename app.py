from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

app=FastAPI()

class ModelInput(BaseModel):
    hours_studied:int
    attendance:int
    sleep_hours:int
    previous_scores:int
    tutoring_sessions:int
    physical_activity:int
    parental_involvement_Low:int
    parental_involvement_Medium:int
    access_to_resources_Low:int
    access_to_resources_Medium: int
    extracurricular_activities_yes:int
    motivation_level_low: int
    motivation_level_medium: int
    internet_access_yes: int
    family_income_low: int
    family_income_medium: int 
    teacher_quality_low:int
    teacher_quality_medium: int
    school_type_public:int
    peer_influence_neutral: int
    peer_influence_positive: int
    learning_disabilities_yes: int
    parental_education_level_high_school: int
    parental_education_level_postgraduate:int
    distance_from_home_moderate:int
    distance_from_home_near: int
    gender_male: int
    
model=pickle.load(open('student_score_model.pkl','rb'))

@app.get("/")
def home():
    return {'massage':'student score model api is running'}

@app.post('/predict')

def predict_student(input_parameter:ModelInput):
    input_list=[
    input_parameter.hours_studied,
    input_parameter.attendance,
    input_parameter.sleep_hours,
    input_parameter.previous_scores,
    input_parameter.tutoring_sessions,
    input_parameter.physical_activity,
    input_parameter.parental_involvement_Low,
    input_parameter.parental_involvement_Medium,
    input_parameter.access_to_resources_Low,
    input_parameter.access_to_resources_Medium ,
    input_parameter.extracurricular_activities_yes,
    input_parameter.motivation_level_low ,
    input_parameter.motivation_level_medium ,
    input_parameter.internet_access_yes ,
    input_parameter.family_income_low ,
    input_parameter.family_income_medium  ,
    input_parameter.teacher_quality_low,
    input_parameter.teacher_quality_medium ,
    input_parameter.school_type_public,
    input_parameter.peer_influence_neutral ,
    input_parameter.peer_influence_positive ,
    input_parameter.learning_disabilities_yes ,
    input_parameter.parental_education_level_high_school ,
    input_parameter.parental_education_level_postgraduate,
    input_parameter.distance_from_home_moderate,
    input_parameter.distance_from_home_near ,
    input_parameter.gender_male 
    ]
    
    prediction=model.predict([input_list])
    
    return {'Predicted Exam Score ':float(prediction[0])}
