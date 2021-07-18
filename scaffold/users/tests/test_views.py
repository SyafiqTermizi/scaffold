import pytest

from scaffold.users.views import UserCreationAPIView


def test_user_creation_api_view_success(db, api_client):
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


@pytest.mark.parametrize(
    "username,email,password_1,password_2,error",
    [
        pytest.param(
            "existinguser",
            "newemail@test.com",
            "matching_password",
            "matching_password",
            {"username": ["A user with that username already exists."]},
        ),
        pytest.param(
            "newusername",
            "existinguser@test.com",
            "matching_password",
            "matching_password",
            {"email": ["user with this email address already exists."]},
        ),
        pytest.param(
            "newusername",
            "newemail@test.com",
            "matching_password",
            "unmatching_password",
            {"non_field_errors": ["Password Not Match"]},
        ),
        pytest.param(
            "",
            "newemail@test.com",
            "matching_password",
            "matching_password",
            {"username": ["This field may not be blank."]},
        ),
        pytest.param(
            "newusername",
            "",
            "matching_password",
            "matching_password",
            {"email": ["This field may not be blank."]},
        ),
        pytest.param(
            "invalidusername!",
            "invalidemail",
            "matching_password",
            "matching_password",
            {
                "username": [
                    "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters."
                ],
                "email": ["Enter a valid email address."],
            },
        ),
    ],
)
def test_user_creation_api_view_fail(
    db,
    api_client,
    create_user,
    username,
    email,
    password_1,
    password_2,
    error,
):
    create_user(username="existinguser", email="existinguser@test.com")

    response = api_client().post(
        "/users/register/",
        data={
            "username": username,
            "email": email,
            "password_1": password_1,
            "password_2": password_2,
        },
        format="json",
    )
    assert response.status_code == 400
    assert response.json() == error
