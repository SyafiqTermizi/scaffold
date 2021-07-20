from typing import Any, Dict

from django.contrib.auth import login
from django.http import Http404
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .models import User, EmailVerificationToken
from .serializers import UserCreationSerializer, AuthenticationSerializer


class UserCreationAPIView(CreateAPIView):
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()


class EmailVerificationTokenView(TemplateView):
    template_name = "users/email_verification_token.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        try:
            EmailVerificationToken.verify_token(token=kwargs["token"])
        except EmailVerificationToken.DoesNotExist:
            raise Http404
        return super().get_context_data(**kwargs)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        login(request=request, user=serializer.user)

        return Response({"msg": "Login successful"})
