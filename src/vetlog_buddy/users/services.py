from vetlog_buddy.users.repository import UserRepository


class UserService:
    def __init__(self, repo: UserRepository, factor: float = 0.5) -> None:
        self.repo = repo
        self.factor = factor

    def is_invalid(self, user) -> bool:
        """Check if user is invalid using logic from filter_username"""
        if len(user.username) == 0:
            return True
        if user.username.isupper():
            return True
        if len(user.username) < 8:
            return True
        if user.uppercase_count / len(user.username) < self.factor:
            return True

        return False

    def remove_invalid(self) -> int:
        """Remove invalid users from the DB, return count"""
        all_users = self.repo.select_all()
        invalid_users = [u for u in all_users if self.is_invalid(u)]
        count = 0
        for user in invalid_users:
            self.repo.delete_user(user)
            count += 1
        print(f"Removed {count} problematic users")
        return count

    def is_suspicious(self, user) -> bool:
        """Check if user is suspicious using logic from suspicious_username"""
        return 0.2 < user.uppercase_count / len(user.username) <= 0.5

    def list_suspicious(self) -> list:
        all_users = self.repo.select_all()
        suspicious_users = [u for u in all_users if self.is_suspicious(u)]
        count = len(suspicious_users)
        print(f"Found {count} suspicious users")
        # return count
        return suspicious_users
