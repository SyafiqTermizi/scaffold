from django.urls import path

from .views import (
    UserCreationAPIView,
    EmailVerificationTokenView,
    LoginView,
    ForgotPasswordView,
    ResetForgotPasswordView,
)

app_name = "users"
urlpatterns = [
    path("register/", UserCreationAPIView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path(
        "forgot-password/",
        ForgotPasswordView.as_view(),
        name="forgot-password",
    ),
    path(
        "reset-forgot-password/<str:uidb64>/<str:token>/",
        ResetForgotPasswordView.as_view(),
        name="reset-forgot-password",
    ),
    path(
        "verify-token/<str:token>/",
        EmailVerificationTokenView.as_view(),
        name="verify-token",
    ),
]
