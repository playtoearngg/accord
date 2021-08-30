from discord_slash import cog_ext, SlashContext
from nextcord.ext.commands import Bot, Cog


class AccordCommands(Cog):
    def __init__(self, db, client: Bot):
        self.db = db
        self.client = client

    @cog_ext.cog_slash(name='ping', guild_ids=[879640837028446248])
    async def _pong(self, ctx: SlashContext):
        await ctx.send('Pong!')
