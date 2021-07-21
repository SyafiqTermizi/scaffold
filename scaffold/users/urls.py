from django.urls import path

from .views import (
    UserCreationAPIView,
    EmailVerificationTokenView,
    LoginView,
    ForgotPasswordView,
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
        "verify-token/<str:token>/",
        EmailVerificationTokenView.as_view(),
        name="verify-token",
    ),
]
