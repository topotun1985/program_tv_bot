from dataclasses import dataclass
from typing import Union
from environs import Env


@dataclass
class DbConfig:
    #host: str
    #password: str
    #user: str
    database: str


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig


def load_config(path: Union[str, None] = None):
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        ),
        db=DbConfig(
            #host=env.str('DB_HOST'),
            #password=env.str('DB_PASS'),
            #user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
    )
