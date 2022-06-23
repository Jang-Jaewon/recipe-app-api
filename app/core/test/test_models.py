"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def teat_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = "test@email.com"
        password = "testpassword123"
        user = get_user_model().objects.crate_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password))
