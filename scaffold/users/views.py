from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import UserCreationSerializer


class UserCreationAPIView(CreateAPIView):
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()
