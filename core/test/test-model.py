from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@superuser.com', 'username', 'firstname', 'lastname', 'password'
        )
        self.assertEqual(super_user.email, 'testuser@superuser.com')
        self.assertEqual(super_user.username, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertEqual(super_user.last_name, 'last_name')
