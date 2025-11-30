import time
import warnings
from datetime import datetime

import pytest
from sqlmodel import Session, SQLModel, create_engine
from testcontainers.mysql import MySqlContainer

# Import your actual classes
from vetlog_buddy.users.models import User
from vetlog_buddy.users.repository import UserRepository
from vetlog_buddy.users.services import UserService

# Filter out testcontainers deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="testcontainers")


@pytest.fixture(scope="session")
def mysql_container():
    """Start a MySQL container for integration testing."""
    container = MySqlContainer("mysql:8.0")
    container.start()
    time.sleep(10)
    yield container
    container.stop()


@pytest.fixture
def session(mysql_container):
    """Create a SQLModel session connected to the test container."""
    connection_url = (
        f"mysql+pymysql://{mysql_container.username}:{mysql_container.password}"
        f"@{mysql_container.get_container_host_ip()}:"
        f"{mysql_container.get_exposed_port(3306)}/{mysql_container.dbname}"
    )
    engine = create_engine(connection_url, echo=True, pool_pre_ping=True)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

    SQLModel.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture
def user_repo(session):
    return UserRepository(session)


@pytest.fixture
def user_service(user_repo):
    return UserService(user_repo)


def populate_example_users(repo: UserRepository):
    users = [
        User(
            id=1,
            account_non_expired=False,
            account_non_locked=False,
            credentials_non_expired=False,
            date_created=datetime.fromisoformat("2024-04-21 20:08:51"),
            email="contact@josdem.io",
            enabled=True,
            first_name="jose",
            last_name="morales",
            mobile=None,
            password="password",
            role="USER",
            username="josdem",
        ),
        User(
            id=2,
            account_non_expired=False,
            account_non_locked=False,
            credentials_non_expired=False,
            date_created=datetime.fromisoformat("2024-04-21 20:08:52"),
            email="contact@josdem.io",
            enabled=True,
            first_name="jose",
            last_name="morales",
            mobile=None,
            password="password",
            role="USER",
            username="johndoe",
        ),
        User(
            id=3,
            account_non_expired=False,
            account_non_locked=False,
            credentials_non_expired=False,
            date_created=datetime.fromisoformat("2024-04-21 20:08:53"),
            email="contact@josdem.io",
            enabled=True,
            first_name="jose",
            last_name="morales",
            mobile=None,
            password="password",
            role="USER",
            username="NHUQfuLarRMDj",
        ),
        User(
            id=4,
            account_non_expired=False,
            account_non_locked=False,
            credentials_non_expired=False,
            date_created=datetime.fromisoformat("2024-04-21 20:08:54"),
            email="contact@josdem.io",
            enabled=True,
            first_name="jose",
            last_name="morales",
            mobile=None,
            password="password",
            role="USER",
            username="rJVyFMNsmXhPUvG",
        ),
    ]
    for u in users:
        repo.add_user(u)


def test_crud_and_service(user_repo: UserRepository, user_service: UserService):
    populate_example_users(user_repo)

    all_users = user_repo.select_all()
    assert len(all_users) == 4
