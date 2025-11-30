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
from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)

    # flags
    account_non_expired: bool
    account_non_locked: bool
    credentials_non_expired: bool
    enabled: bool

    # timestamps
    date_created: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # personal
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    mobile: str | None = Field(default=None)
    username: str = Field(index=True, unique=True, nullable=False)

    # auth
    password: str
    role: str

    @property
    def uppercase_count(self) -> int:
        return sum(1 for char in self.username if char.isupper())

    @property
    def uppercase_ratio(self) -> float:
        return self.uppercase_count / len(self.username)

    # This probably belongs here, but I want to keep the two (invalid/suspicous) checks together

    # @property
    # def suspicious(self) -> bool:
    #     """Detects if the username is suspicious based on uppercase ratio"""
    #     return 0.2 < self.uppercase_ratio <= 0.5
