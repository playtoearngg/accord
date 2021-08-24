from .helpers import add_thread_emoji
from discord import Client


class AccordClient(Client):
    async def on_ready(self):
        # Hello, world
        print('Logged on as {0}!'.format(self.user))

    async def on_thread_join(self, thread):
        # On thread create
        await thread.edit(locked=True)          # Only mods can archive/unarchive
        await add_thread_emoji(thread)
