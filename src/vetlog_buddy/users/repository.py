from collections.abc import Sequence

from sqlmodel import Session, select

from vetlog_buddy.users.models import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def add_user(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def select_all(self) -> Sequence[User]:
        # return list(self.session.exec(select(User)).all())
        return self.session.exec(select(User)).all()

    def select_username(self, username: str) -> User | None:
        return self.session.exec(select(User).where(User.username == username)).first()

    def delete_user(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()
