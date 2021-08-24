from .helpers import add_thread_emoji
from discord import Client


class AccordClient(Client):
    # Hello, world
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # On thread create
    async def on_thread_join(self, thread):
        # Add thread emoji to title
        await add_thread_emoji(thread)

        # Only mods can archive/unarchive
        await thread.edit(locked=True)
