from django.urls import path

from .views import UserCreationAPIView, EmailVerificationTokenView, LoginView

app_name = "users"
urlpatterns = [
    path("register/", UserCreationAPIView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path(
        "verify-token/<str:token>/",
        EmailVerificationTokenView.as_view(),
        name="verify-token",
    ),
]
