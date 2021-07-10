import factory
from factory.django import DjangoModelFactory

from scaffold.users.models import User


class UserFactory(DjangoModelFactory):
    username = factory.Faker("name")
    email = factory.Faker("email")

    class Meta:
        model = User
