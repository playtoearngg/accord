from cogs.helpers import add_thread_emoji
from nextcord import Activity, ActivityType
from nextcord.ext import tasks
from nextcord.ext.commands import Bot, Cog


class AccordLoop(Cog):
    def __init__(self, accord_client: Bot):
        self.client = accord_client
        self.main.start()

    # Run housekeeping every 5 min
    @tasks.loop(seconds=300)
    async def main(self):
        if not self.client.is_closed():
            await self.update_presence()
            await self.do_guilds()

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

    # General housekeeping for all guilds
    async def do_guilds(self):
        for guild in self.client.guilds:
            # Threads housekeeping
            for thread in guild.threads:
                # Unarchive thread if not manually archived by a mod
                if thread.archived and not thread.name.startswith('🗑️'):
                    await thread.edit(archived=False)

                # Add thread emoji to all threads in history
                await add_thread_emoji(thread)

                # Set all threads to locked so only mods can (un)archive
                await thread.edit(locked=True)

            # Channels housekeeping
            # Only allow @everyone to message threads, not channels
            for channel in guild.text_channels:
                perms = channel.overwrites_for(guild.default_role)
                perms.send_messages = False
                perms.send_messages_in_threads = True
                await channel.set_permissions(guild.default_role, overwrite=perms)
