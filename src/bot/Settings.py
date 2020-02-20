from os import path
import json


class Settings(object):
    def __init__(self):
        self.discord_secret = ""
        self.channel = ""
        self.guild = ""


def load_discord_secret(settings: Settings):
    if not path.exists("discordSecret"):
        raise FileNotFoundError("Missing discord secret file!")

    with open("discordSecret", "r") as f:
        settings.discord_secret = f.read()


def load_channel_guild(settings: Settings):
    if not path.exists("config.json"):
        raise FileNotFoundError("Missing config.json file")

    with open("config.json", "r") as f:
        json_content = json.loads(f.read())
        settings.guild = json_content["guild"]
        settings.channel = json_content["channel"]


def load_settings() -> Settings:
    settings = Settings()
    load_channel_guild(settings)
    load_discord_secret(settings)
    return settings
