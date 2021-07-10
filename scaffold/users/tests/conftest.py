import pytest
from scaffold.users.tests.factories import UserFactory


@pytest.fixture
def create_user():
    def fn(**kwargs):
        return UserFactory.create(**kwargs)

    return fn
