from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class Token_generator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return {
            text_type(user.pk) + text_type(timestamp)
        }


token_generator = Token_generator()
