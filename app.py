from discord_slash import SlashCommand, SlashContext
from cogs.helpers import add_thread_emoji, get_var
from nextcord import Intents, Embed, Message, TextChannel, Thread
from nextcord.ext.commands import Bot


# Instantiate Discord client and slash commands
accord = Bot(command_prefix='a.', intents=Intents.default())
slash = SlashCommand(accord, sync_commands=True)


@slash.slash(name="test", guild_ids=[879640837028446248])
async def _test(ctx: SlashContext):
    await ctx.defer()
    print('Attempting reply')
    embed = Embed(title="Embed Test")
    await ctx.send(embed=embed)


# Hello, world
@accord.event
async def on_ready():
    print('Logged on as {0}!'.format(accord.user))


# On message
@accord.event
async def on_message(message: Message):
    # Auto pin messages in channels
    if isinstance(message.channel, TextChannel) and not message.is_system():
        await message.pin()


# On thread create
@accord.event
async def on_thread_join(thread: Thread):
    # Add thread emoji to title
    await add_thread_emoji(thread)

    # Only mods can archive/unarchive
    await thread.edit(locked=True)


# On slash command
@accord.event
async def on_slash_command(ctx: SlashContext):
    print(ctx)


# Load cogs and run bot
accord.load_extension("cogs")
accord.run(get_var('DISCORD_TOKEN'))
