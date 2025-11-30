import pytest

from vetlog_buddy.users.models import User
from vetlog_buddy.users.services import UserService


class DummyRepo:
    """A placeholder repo so the service can be instantiated."""


@pytest.mark.parametrize(
    "username,expected",
    [
        ("josdem", False),
        ("johndoe", False),
        ("IRIS", False),
        ("Max", True),
        ("Jc", True),
        ("NHUQfuLarRMDj", False),
        ("rJVyFMNsmXhPUvG", False),
        ("rVhBLNPSNIPE", False),
        ("SxeQsgXI", True),
        ("NDDmMAUftYXkxO", False),
    ],
)
def test_is_suspicious(username, expected):
    service = UserService(repo=DummyRepo(), factor=0.5)

    user = User(
        id=1,
        email="test@example.com",
        is_enabled=True,
        first_name="X",
        last_name="Y",
        password="secret",
        role="USER",
        username=username,
    )

    assert service.is_suspicious(user) == expected
