from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@superuser.com', 'firstname', 'lastname', 'username1', '+2348108335923', 'password'
        )
        self.assertEqual(super_user.email, 'testuser@superuser.com')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertEqual(super_user.last_name, 'username1')
        self.assertEqual(super_user.username, 'lastname')
        self.assertEqual(super_user.phone_number, '+2348108335923')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertTrue(str(super_user), "email")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testuser@super.com", username="username1", first_name="first_name", last_name="last_name", phone_number="+2348108335923", password="password", is_superuser=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testuser@super.com", username="username1", first_name="first_name", last_name="last_name", phone_number="+2348108335923", password="password", is_staff=False,
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="", username="username1", first_name="first_name", last_name="last_name", phone_number="+2348108335923", password="password", is_staff=False,
            )

    def test_new_user(self):
            db = get_user_model()
            user = db.objects.create_user(
                'testuser@user.com', 'firstname', 'username', 'lastname','+2348119464410', 'password'
            )
            self.assertEqual(user.email, 'testuser@user.com')
            self.assertEqual(user.username, 'username')
            self.assertEqual(user.first_name, 'firstname')
            self.assertEqual(user.last_name, 'lastname')
            self.assertEqual(user.phone_number,'+2348119464410')
            self.assertFalse(user.is_superuser)
            self.assertFalse(user.is_staff)
            self.assertFalse(user.is_active)

            with self.assertRaises(ValueError):
                db.objects.create_user(
                    email="", username="username1", first_name="first_name", last_name="last_name", phone_number="+2348108335923", password="password", is_superuser=True,
            )

            
       
            

           
