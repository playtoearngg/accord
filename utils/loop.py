from .helpers import add_thread_emoji
from nextcord import Activity, ActivityType, Client
from nextcord.ext import tasks


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

    # Discord presence
    async def update_presence(self):
        # Count users in all guilds
        num_users = 0
        for guild in self.client.guilds:
            # Don't count this bot
            num_users += guild.member_count - 1

        activity = Activity(name=f'{num_users} users', type=ActivityType.listening)
        await self.client.change_presence(activity=activity)

    # Threads housekeeping
    async def do_threads(self):
        for guild in self.client.guilds:
            for thread in await guild.active_threads():
                # Add thread emoji to all threads in history
                await add_thread_emoji(thread)

                # Set all threads to locked so only mods can (un)archive
                await thread.edit(locked=True)
