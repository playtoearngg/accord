from .helpers import add_thread_emoji
from discord import Client
from discord.ext import tasks


class AccordLoop:
    def __init__(self, accord_client: Client):
        self.client = accord_client

    # Run housekeeping every 5 min
    @tasks.loop(seconds=300)
    async def main(self):
        while not self.client.is_closed():
            await self.do_threads()

    # Wait until client is ready before housekeeping
    @main.before_loop
    async def before_main(self):
        await self.client.wait_until_ready()

    # Threads housekeeping
    async def do_threads(self):
        for guild in self.client.guilds:
            for thread in await guild.active_threads():
                # Add thread emoji to all threads in history
                await add_thread_emoji(thread)

                # Set all threads to locked so only mods can (un)archive
                await thread.edit(locked=True)
