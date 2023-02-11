from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()    # Создаем экземпляр класса Env
    # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
