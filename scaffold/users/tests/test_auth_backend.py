from django.http import request
import pytest
from django.contrib.auth import authenticate

from scaffold.users.auth_backends import EmailBackend


def test_auth_backend(db, rf, create_user):
    """
    Auth backend should be able to get user via email
    """
    request = rf.get("/")
    user = create_user()
    user.set_password("test123")
    user.save()

    backend = EmailBackend()
    authenticated_user = backend.authenticate(
        request=request,
        email=user.email,
        password="test123",
    )
    assert authenticated_user.username == user.username


def test_authenticate_with_email(db, rf, create_user):
    """
    Calling authenticate with email, should return the correct user
    """
    request = rf.get("/")
    user = create_user()
    user.set_password("test123")
    user.save()

    authenticated_user = authenticate(
        request=request, email=user.email, password="test123"
    )
    assert authenticated_user.username == user.username
