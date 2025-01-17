from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAuthBackend(ModelBackend):
    """
    Custom authentication backend to allow login with email instead of username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Authenticate using the email field
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
