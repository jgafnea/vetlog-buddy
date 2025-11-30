#  Copyright 2025 Jose Morales contact@josdem.io
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License
from datetime import datetime

from sqlmodel import Field, SQLModel

"""
Schema taken from CI

Replaces
database_connector.py
database_filter.py
filter_username.py
suspicious_username.py
user_filter.py
user_remover.py
"""


class User(SQLModel, table=True):
    # __tablename__ = "user"
    id: int = Field(default=None, primary_key=True)
    account_non_expired: bool
    account_non_locked: bool
    credentials_non_expired: bool
    date_created: datetime
    email: str | None = None
    enabled: bool
    first_name: str | None = None
    last_name: str | None = None
    mobile: str | None = None
    password: str
    role: str
    username: str

    @property
    def uppercase_count(self) -> int:
        """Number of uppercase characters in username"""
        return sum(1 for char in self.username if char.isupper())

    @property
    def uppercase_ratio(self) -> float:
        """Ratio of uppercase characters in username"""
        return self.uppercase_count / len(self.username)
