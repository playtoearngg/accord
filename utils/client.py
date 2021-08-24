from .helpers import add_thread_emoji
from discord.ext.commands import Bot
from discord import Message, TextChannel


class AccordClient(Bot):
    # Hello, world
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # On message
    async def on_message(self, message: Message):
        # Auto pin messages in channels
        if message.channel is TextChannel:
            await message.pin()

    # On thread create
    async def on_thread_join(self, thread):
        # Add thread emoji to title
        await add_thread_emoji(thread)

        # Only mods can archive/unarchive
        await thread.edit(locked=True)
