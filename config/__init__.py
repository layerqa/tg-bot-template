from configparser import ConfigParser

from .config import Telegram, Database, Config


def get_config() -> Config:
    """Get config func"""
    config_data = ConfigParser()
    config_data.read(filenames="config.ini")
    return Config(
        telegram=Telegram(**config_data["telegram"]),
        database=Database(**config_data["database"])
    )