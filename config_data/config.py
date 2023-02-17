from environs import Env


class TgBot:
    # token: str
    def __init__(self, token) -> None:
        self.token = token


class Config:
    # tg_bot: TgBot
    def __init__(self, tg_bot) -> None:
        self.tg_bot = tg_bot


def load_config(path: str | None = None) -> Config:
    env = Env()    # Создаем экземпляр класса Env
    # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
