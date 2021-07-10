import pytest
from rest_framework import serializers

from scaffold.users.serializers import UserCreationSerializer


def test_serializer_validate_invalid_email(db, create_user):
    """
    UserCreationSerializer should raise validation error if input with existing
    email is given
    """
    user = create_user()
    serializer = UserCreationSerializer(
        data={
            "username": "user.username",
            "email": user.email,
            "password_1": "password123321",
            "password_2": "password123321",
        }
    )

    with pytest.raises(serializers.ValidationError):
        serializer.is_valid(raise_exception=True)


def test_serializer_validate_invalid_username(db, create_user):
    """
    UserCreationSerializer should raise validation error if input with existing
    username is given
    """
    user = create_user()
    serializer = UserCreationSerializer(
        data={
            "username": user.username,
            "email": "email@emtail.com",
            "password_1": "password123321",
            "password_2": "password123321",
        }
    )

    with pytest.raises(serializers.ValidationError):
        serializer.is_valid(raise_exception=True)


def test_serializer_validate_password(db, create_user):
    """
    UserCreationSerializer should raise validation error if password_1 and password_2
    not matched
    """
    user = create_user()
    serializer = UserCreationSerializer(
        data={
            "username": "user.username",
            "email": "email@email.com",
            "password_1": "password123321a",
            "password_2": "password123321",
        }
    )

    with pytest.raises(serializers.ValidationError):
        serializer.is_valid(raise_exception=True)


def test_serializer_valid_data(db, create_user):
    """
    UserCreationSerializer should not raise validation error if
    1. Username does not already exist
    2. Email does not already exist
    3. Password 1 and password 2 are matched
    """
    serializer = UserCreationSerializer(
        data={
            "username": "user.username",
            "email": "email@email.com",
            "password_1": "password123321",
            "password_2": "password123321",
        }
    )

    assert serializer.is_valid(raise_exception=True)
    assert serializer.save()
