import requests
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

################ RESPONSE TO API #####################
RESPONSE = requests.get('https://itsocialapp.azurewebsites.net/newsapi').json()

################ TOKEN #####################


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)


generate_token = TokenGenerator()



