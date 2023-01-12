
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class SettingsBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.
    Use the login name and a hash of the password. For example:
    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    Each user has the following attributes:
    ['id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']
    """

    def authenticate(request, username=None, password=None):
        login_valid = False
        user_list = User.objects.raw("SELECT * FROM auth_user")
        if (len(user_list) > 0):
            user = user_list[0]
            algorithm, iterations, salt, hash = user.password.split('$', 3)
            query = "SELECT * FROM auth_user WHERE username = '%s' and password='%s'" % (username, make_password(password, salt=salt))
            login_valid = len(User.objects.raw(query)) > 0

        if login_valid:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

       