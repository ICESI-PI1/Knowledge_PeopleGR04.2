from django.contrib.auth import get_user_model
from django.test import TestCase
from users.models import User


class UsersManagersTests(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(email="normal@user.com", password="foo", name="little user", idType=1,numID=123456789,role=1)
        self.assertEqual(user.email, "normal@user.com")
        user.email = "carjabo12@gmail.com"
        self.assertEqual(user.email, "carjabo12@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_noncreate_user(self):    
        try:
            user = User.objects.create_user(email="normal12@user.com", password="foo12", name="", idType=1,numID=12345678999,role=1)
            #self.assertFalse(user.is_active)
        except: 
            self.assertFalse(user.is_active)
    
    



    '''
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.email)
            #self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")
    '''        
    '''
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False)
    '''

   