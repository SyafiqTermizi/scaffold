import factory
from factory.django import DjangoModelFactory

from scaffold.users.models import User, EmailVerificationToken


class UserFactory(DjangoModelFactory):
    username = factory.Faker("name")
    email = factory.Faker("email")

    class Meta:
        model = User


class EmailVerificationTokenFactory(DjangoModelFactory):
    token = factory.Faker("paragraph")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = EmailVerificationToken
