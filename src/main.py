import discord
from discord.enums import ChannelType
from datetime import datetime


TARGET_CHANNEL = "general"

MONDAY = 0     # -
TUESDAY = 1    # 1
WEDNESDAY = 2  # -
THURSDAY = 3   # 1
FRIDAY = 4     # -
SATURDAY = 5   # 2
SUNDAY = 6     # 1

SERVER_RESET = 10

WAR_DAYS = [
    MONDAY,
    WEDNESDAY,
    FRIDAY
]

POST_WAR_DAYS = [
    TUESDAY,
    THURSDAY,
    SATURDAY,
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
        now = self.get_datetime()
        hours = now.hour + (now.minute / 60)

        if now.weekday() in WAR_DAYS and hours > SERVER_RESET:
            return True
        elif now.weekday() in POST_WAR_DAYS and hours < SERVER_RESET:
            return True
        else:
            return False

    def time_to_war(self) -> int:
        return 0

    def time_to_end(self) -> int:
        return 0

    def days_to_war(self, day) -> int:
        if day == FRIDAY:
            return 3
        elif day == SATURDAY:
            return 2
        else:
            return 1

    async def message_war_end(self, channel):
        await channel.send("We're at war!")

    async def message_war_start(self, channel):
        now = self.get_datetime()
        day = now.weekday()
        days_to_war = self.days_to_war(day)

        await channel.send("We're not at war")

        pass

    async def on_ready(self):
        target_channel = self.get_target_channel()
        if target_channel is None:
            print("ERROR: failed to find target channel")
            await self.close()

        if self.is_at_war():
            await self.message_war_end(target_channel)
        else:
            await self.message_war_start(target_channel)

        await self.close()


if __name__ == "__main__":
    f = open("./discordSecret")
    discordSecret = f.read()
    f.close()

    client = Yuna()
    client.run(discordSecret)
