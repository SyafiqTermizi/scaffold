from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    is_email_verified = models.BooleanField(
        _("verified email"),
        default=False,
        help_text=_("Designates whether the user has verified their email address"),
    )

    def __str__(self) -> str:
        return self.username
