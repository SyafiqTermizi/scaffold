from typing import Any, Optional

from django.contrib.auth.backends import ModelBackend
from django.http.request import HttpRequest

from scaffold.users.models import User


class EmailBackend(ModelBackend):
    """
    Authenticates using Email address
    """

    def authenticate(
        self,
        request: HttpRequest,
        email: Optional[str],
        password: Optional[str],
        **kwargs: Any
    ) -> Optional[User]:
        if email is None or password is None:
            return
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
