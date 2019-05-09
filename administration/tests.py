from django.test import TestCase

from social_django.models import UserSocialAuth

from .models import User
from .forms import UserForm


class AdministrationTests(TestCase):
    def setUp(self):
        self.administrator = User.objects.create_user(
            username='user', password='user', is_staff=True)

    def test_creation_of_user_without_username_sets_uuid_in_username(self):
        user = User.objects.create(first_name="test", last_name="test")
        self.assertIsNotNone(user.username)

    def test_creation_of_user_by_social_sets_user_is_staff(self):
        user = User.objects.create(first_name="test", last_name="test")
        user_auth = UserSocialAuth.objects.create(user=user,
                                                  provider="test",
                                                  uid="test")
        self.assertTrue(user_auth.user.is_staff)

    def test_valid_user_form(self):
        user = User.objects.create(
            first_name="test", last_name="test", iban="DE89370400440532013000")
        data = {'first_name': user.first_name,
                'last_name': user.last_name, 'iban': user.iban, }
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_user_form_formated_iban(self):
        user = User.objects.create(
            first_name="test", last_name="test", iban="DE89 3704 0044 0532 0130 00")
        data = {'first_name': user.first_name,
                'last_name': user.last_name, 'iban': user.iban, }
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_form_without_iban(self):
        user = User.objects.create(
            first_name="test", last_name="test")
        data = {'first_name': user.first_name,
                'last_name': user.last_name, }
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_user_form_with_invalid_iban(self):
        user = User.objects.create(
            first_name="test", last_name="test", iban="DE54 3704 0044 0532 0130 00")
        data = {'first_name': user.first_name,
                'last_name': user.last_name, 'iban': user.iban, }
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())
