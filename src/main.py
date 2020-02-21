from bot.Yuna import Yuna
from bot.Settings import load_settings
from bot import Message


async def on_ready(client: Yuna):
    messages = Message.get_message()

    for message in messages:
        await client.write(message)
    await client.stop()


def main():
    settings = load_settings()

    client = Yuna(settings, on_ready)
    client.run(settings.discord_secret)


if __name__ == "__main__":
    main()
