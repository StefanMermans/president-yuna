import discord
from discord.enums import ChannelType
from datetime import datetime


TARGET_CHANNEL = "general"

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

SERVER_RESET = 10

WAR_DAYS = [
    MONDAY,
    WEDNESDAY,
    FRIDAY
]


class Yuna(discord.Client):
    def get_target_channel(self):
        channels = self.get_all_channels()
        for channel in channels:
            if channel.type == ChannelType.text and channel.name == TARGET_CHANNEL:
                return channel
        return None

    def get_datetime(self):
        return datetime.utcnow()

    def is_at_war(self):
        return self.get_datetime().weekday() in WAR_DAYS

    def time_to_war(self) -> int:
        return 0

    def time_to_end(self) -> int:
        return 0

    def days_to_war(self, start_day) -> int:
        if start_day == SATURDAY:
            return 2
        else:
            return 1



    async def message_war_end(self, channel):
        pass

    async def message_war_start(self, channel):
        now = self.get_datetime()
        day = now.weekday()
        days_to_war = self.days_to_war(day)

        pass

    async def on_ready(self):
        target_channel = self.get_target_channel()
        if target_channel is None:
            print("ERROR: failed to find target channel")
            await self.close()

        if self.is_at_war():
            await self.message_war_end(target_channel)
        else:
            await self.message_war_end(target_channel)

        await self.close()


client = Yuna()
client.run('')
