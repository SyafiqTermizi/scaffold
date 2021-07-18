from django.urls import path

from .views import UserCreationAPIView, EmailVerificationTokenView

app_name = "users"
urlpatterns = [
    path("register/", UserCreationAPIView.as_view(), name="register"),
    path(
        "verify-token/<str:token>/",
        EmailVerificationTokenView.as_view(),
        name="verify-token",
    ),
]
