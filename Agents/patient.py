import yaml
import random

class Patient:
    def __init__(self, patient_ID, age, gender, ref_spec, plan_adm,
                 admission_date, treatment_duration, municipality):
        
        self.patient_ID = patient_ID
        self.age = age
        self.gender = gender
        self.ref_spec = ref_spec
        self.plan_adm = plan_adm
        self.admission_date = admission_date
        self.treatment_duration = treatment_duration
        # self.municipality = municipality

        # with open('config.yaml', 'r') as file:
        #     self.conf = yaml.safe_load(file)