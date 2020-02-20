import discord
from discord.enums import ChannelType
from bot.Settings import Settings


class Yuna(discord.Client):
    def __init__(self, settings: Settings, on_ready_callback, **options):
        super().__init__(**options)
        self.settings = settings
        self.on_ready_callback = on_ready_callback

    def get_target_channel(self):
        channels = self.get_all_channels()
        for channel in channels:
            if channel.type == ChannelType.text \
                    and channel.name == self.settings.channel \
                    and channel.guild.name == self.settings.guild:
                return channel
        return None

    async def stop(self):
        await self.close()

    async def write(self, message: str):
        target_channel = self.get_target_channel()
        if target_channel is None:
            print("ERROR: failed to find target channel")
            await self.close()
        await target_channel.send(message)

    async def on_ready(self):
        await self.on_ready_callback(self)
