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

    def get_all(self) -> list[User]:
        return list(self.session.exec(select(User)).all())

    def get_by_username(self, username: str) -> User | None:
        return self.session.exec(select(User).where(User.username == username)).first()

    def delete(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()
