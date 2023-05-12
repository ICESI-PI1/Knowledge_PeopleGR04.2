from django.contrib.auth import get_user_model
from django.test import TestCase
from users.models import User

    
class UserTest(TestCase):
     def setUp(self):
        user = User()
        return user
     
     def test_scenario_1(self):
        try:
            user = self.setUp()
        except:
            print("User object didn't create")
        
     def test_scenario_2(self):
            user = self.setUp()
            user.email = "john@example.com"
            user.password = "johndoe1"
            user.name = "John Doe"
            user.idType = 1
            user.numID = "112508374"
            user.role = 1

            self.assertEqual(user.email,"john@example.com")

     def test_scenario_3(self):
            user = self.setUp()
            self.assertEqual(user.email,"")
            user.email = "test@test.com"
            user.password = "janesmith"
            user.name = "Jane Smith"
            user.idType = "Driver's License"
            user.numID = "1234567890"
            user.role = "Admin"

            self.assertNotEqual(user.email,"john@example.com")

