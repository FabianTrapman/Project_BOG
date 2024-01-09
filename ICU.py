from Agents.patient import generate_random_patient

class ICUUnit:
    def __init__(self, bed_capacity, specialization):
        self.bed_capacity = bed_capacity
        self.specialization = specialization
        self.current_patients = []

    def admit_patients(self, num_admissions):
        for _ in range(num_admissions):
            patient = generate_random_patient()

            if len(self.current_patients) < self.bed_capacity:
                self.current_patients.append(patient)

    def update_simulation(self):
        discharged_patients = []
        for patient in self.current_patients:
            patient.treatment_duration -= 1
            if patient.treatment_duration <= 0:
                discharged_patients.append(patient)

        for patient in discharged_patients:
            self.current_patients.remove(patient)