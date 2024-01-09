import random
import matplotlib.pyplot as plt
from ICU import ICUUnit

class ICUSimulation:
    def __init__(self, icu_units):
        self.icu_units = icu_units
        self.admission_log = []

    def run_simulation(self, num_days):
        for day in range(num_days):
            daily_admissions = self.generate_daily_admissions()
            self.admit_patients(daily_admissions)
            self.update_simulation()
            self.admission_log.append(sum(len(icu.current_patients) for icu in self.icu_units))

    def generate_daily_admissions(self):
        return [icu.generate_daily_admissions() for icu in self.icu_units]

    def admit_patients(self, daily_admissions):
        for icu, num_admissions in zip(self.icu_units, daily_admissions):
            icu.admit_patients(num_admissions)

    def update_simulation(self):
        for icu in self.icu_units:
            icu.update_simulation()

    def plot_simulation_results(self):
        for i, icu in enumerate(self.icu_units):
            plt.plot(range(len(self.admission_log)), [day[i] for day in self.admission_log], label=f'ICU {icu.specialization}')

        plt.xlabel('Days')
        plt.ylabel('Number of Patients')
        plt.title('ICU Simulation Results')
        plt.legend()
        plt.show()

# Example usage:
icu_units = [
    ICUUnit(bed_capacity=10, specialization='Cardiology'),
    ICUUnit(bed_capacity=8, specialization='Neurology'),
    ICUUnit(bed_capacity=12, specialization='Trauma')
]

simulation = ICUSimulation(icu_units)
simulation.run_simulation(num_days=30)
simulation.plot_simulation_results()
