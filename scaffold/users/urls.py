from django.urls import path

from .views import UserCreationAPIView

app_name = "users"
urlpatterns = [
    path("register/", UserCreationAPIView.as_view(), name="register"),
]
