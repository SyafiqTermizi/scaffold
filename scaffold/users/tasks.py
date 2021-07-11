from celery import shared_task

from .models import User, EmailVerificationToken


@shared_task
def create_token_and_send_email(user_id: int):
    user: User = User.objects.get(pk=user_id)
    token: EmailVerificationToken = EmailVerificationToken.objects.create(user=user)

    message = f"""
    Hi {user.username},
    We're happy you signed up for Scaffold. To start exploring the app, please
    confirm your email address.

    {token.token}

    Welcome to Scaffold!
    The Scaffold Team
    """

    user.email_user(
        "Email Verification",
        message=message,
        from_email="no-reply@scaffold.com",
    )
