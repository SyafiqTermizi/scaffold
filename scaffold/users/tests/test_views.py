import pytest

from scaffold.users.views import UserCreationAPIView


def test_user_creation_api_view(db, api_client):
    """
    If a user creation is successful, the endpoint should:
    1. return status 201
    2. return a JSON that contains username and email only
    """
    response = api_client().post(
        "/users/register/",
        data={
            "username": "test",
            "email": "test@example.com",
            "password_1": "password123321",
            "password_2": "password123321",
        },
        format="json",
    )
    assert response.status_code == 201
    assert response.json()["username"] == "test"
    assert response.json()["email"] == "test@example.com"

    with pytest.raises(KeyError):
        response.json()["password_1"]
