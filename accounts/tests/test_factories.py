from django.contrib.auth import get_user_model
from django.test import TestCase

from faker import Faker

from accounts import factories


class UserFactoryTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.fake = Faker()
        cls.user_password = cls.fake.password()
        cls.user = factories.UserFactory(password=cls.user_password)

    def test_object_creation(self):
        self.assertEqual(get_user_model().objects.count(), 1)

    def test_is_staff(self):
        self.assertFalse(self.user.is_staff)

    def test_username(self):
        username = self.user.username
        self.assertGreaterEqual(len(username), 5)

    def test_email(self):
        email = self.user.email
        self.assertGreaterEqual(len(email), 7)
        self.assertIn("@", email)

    def test_password(self):
        password = self.user_password
        self.assertEqual(len(password), 10)


class AdminUserFactoryTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = factories.AdminUserFactory()

    def test_user_is_staff(self):
        staff_users = get_user_model().objects.filter(is_staff=True)
        self.assertTrue(self.user.is_staff)
        self.assertEqual(len(staff_users), 1)

    def test_user_is_superuser(self):
        superusers = get_user_model().objects.filter(is_superuser=True)
        self.assertTrue(self.user.is_superuser)
        self.assertEqual(len(superusers), 1)
