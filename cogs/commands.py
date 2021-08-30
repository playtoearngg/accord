from nextcord.ext.commands import Bot, Cog, command, Context
from nextcord import Embed, Thread


class AccordCommands(Cog):
    def __init__(self, client: Bot, db):
        self.client = client
        self.db = db

    @command(name='ping')
    async def ping(self, ctx: Context):
        await ctx.send('Pong! {}ms'.format(round(self.client.latency * 1000, 2)))

    @command(name='archivethread', aliases=['at'])
    async def archive_thread(self, ctx: Context):
        if isinstance(ctx.channel, Thread):
            print('Archiving thread {}'.format(ctx.channel.id))
            # Rename thread first so we don't auto unarchive it
            if not ctx.channel.name.startswith('🗑️'):
                await ctx.channel.edit(name='{0}{1}'.format('🗑️', ctx.channel.name))

            await ctx.channel.edit(archived=True)
        else:
            embed = Embed(title='You can only run this command in a thread.')
            await ctx.send(embed=embed)
