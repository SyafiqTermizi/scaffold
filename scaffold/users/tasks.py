from celery import shared_task
from django.conf import settings
from django.urls import reverse

from .models import User, EmailVerificationToken


@shared_task
def create_token_and_send_email(user_id: int):
    user = User.objects.get(pk=user_id)
    token = EmailVerificationToken.objects.create(user=user)
    token_verify_url = reverse("users:verify-token", kwargs={"token": token.token})

    if settings.DEBUG:
        full_url = f"http://localhost:8000{token_verify_url}"
    else:
        full_url = f"{settings.ALLOWED_HOSTS[0]}/{token_verify_url}"

    message = f"""
    Hi {user.username},

    We're happy you signed up for Scaffold. To start exploring the app, please confirm your email address.
    
    {full_url}

    Welcome to Scaffold!
    The Scaffold Team
    """

    user.email_user(
        "Email Verification",
        message=message,
        from_email="no-reply@scaffold.com",
    )
