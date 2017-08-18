from account import hooks
from django.contrib.auth.models import User


class BetterAccountHookSet(hooks.AccountDefaultHookSet):

    def get_user_credentials(self, form, identifier_field):
        username = form.cleaned_data[identifier_field]

        # Find an actual username so we can authenticate
        print username,
        if identifier_field == "email":
            username = self.get_username_by_email(username)
        print username,

        return {
            "username": username,
            "password": form.cleaned_data["password"],
        }

    def get_username_by_email(self, email):

        try:
            return User.objects.get(email=email).username
        except User.DoesNotExist:
            return None
