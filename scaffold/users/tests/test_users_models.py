import pytest


def test_user_model_str_method(db, create_user):
    """__str__ method should return username"""

    user = create_user()
    assert user.__str__() == user.username
