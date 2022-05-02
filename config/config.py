from dataclasses import dataclass


@dataclass
class Telegram:
    bot_token: str
    admin_id: int

    def __post_init__(self) -> None:
        """Convert types"""
        self.admin_id = int(self.admin_id)

@dataclass
class Database:
    host: str
    port: int
    user: str
    password: str
    name: str

    def __post_init__(self) -> None:
        """Convert types"""
        self.port = int(self.port)

@dataclass
class Config:
    telegram: Telegram
    database: Database