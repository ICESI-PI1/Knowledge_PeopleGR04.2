from django.test import TestCase
from scholarships.models import Scholarship

class ScholarshipTest(TestCase):
     def setUp(self):
        scholarship = Scholarship()
        return scholarship
     
     def test_scenario_1(self):
        try:
            scholarship = self.setUp()
        except:
            print("Scholarship object didn't create")
        
     def test_scenario_2(self):
            scholarship = self.setUp()
            scholarship.stratum = 5
            scholarship.motivational_letter = "Hola, me gustaria tener beca."
            scholarship.value_period = 15000
            scholarship.icfes_score = 420
            scholarship.period_current = 6
            scholarship.program_adm = "Ingeniería de Sistemas"
            scholarship.application_type = 'A'
            scholarship.state = 'P'
            scholarship.total_periods = 10
            scholarship.active = 'AC'

            self.assertEqual(scholarship.motivational_letter,"Hola, me gustaria tener beca.")

     def test_scenario_2(self):
            scholarship = self.setUp()
            scholarship.stratum = 1
            scholarship.motivational_letter = "Hola, me quisiera hacer parte de estos programas y desarrollarme integramente  ."
            scholarship.value_period = 20000
            scholarship.icfes_score = 350
            scholarship.period_current = 1
            scholarship.program_adm = "Ingeniería de Sistemas"
            scholarship.application_type = 'NI'
            scholarship.state = 'P'
            scholarship.total_periods = 10
            scholarship.active = 'AC'

            
            self.assertNotEqual(scholarship.stratum, 4)

        

            