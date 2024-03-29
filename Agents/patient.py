import yaml
import random

class Patient:
    def __init__(self, patient_ID, age, gender, ref_spec, plan_adm,
                 admission_date, treatment_duration, municipality):
        
        '''
        Clarification of a few parameters
        ref_spec           = the specialisation of that unit (string)
                             usually refers to type of ailment
        plan_adm           = planned/unplanned admission     (bool)
        admission date     = day of admission (730 days)     (int)
        treatment duration = duration of treatment in days   (int)
        '''
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