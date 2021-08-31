from cogs.helpers import add_thread_emoji, get_var, lock_channel
from nextcord.abc import GuildChannel
from nextcord import Intents, Message, TextChannel, Thread
from nextcord.ext.commands import Bot


# Instantiate Discord client
prefix = 'a/'
accord = Bot(command_prefix=prefix, intents=Intents.default())


# Hello, world
@accord.event
async def on_ready():
    print('Logged on as {0}!'.format(accord.user))


# On message
@accord.event
async def on_message(message: Message):
    # Ignore messages sent by this bot
    if message.author == accord.user:
        return

    # Is this a command?
    if message.content.startswith(prefix):
        await accord.process_commands(message)
    else:
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


# On thread update
@accord.event
async def on_thread_update(before: Thread, after: Thread):
    # If manually unarchived, remove wastebasket emoji
    if before.archived and not after.archived:
        print('Thread {} unarchived'.format(before.id))
        if before.name.startswith('🗑️'):
            print('Renaming thread {}'.format(after.id))
            await after.edit(name=after.name[1:])


# On channel create
@accord.event
async def on_guild_channel_create(channel: GuildChannel):
    if isinstance(channel, TextChannel):
        print('Locking new channel {}'.format(channel.id))
        await lock_channel(channel)


# On channel update
@accord.event
async def on_guild_channel_update(_: GuildChannel, after: GuildChannel):
    if isinstance(after, TextChannel):
        print('Locking updated channel {}'.format(after.id))
        await lock_channel(after)


# Load cogs and run bot
accord.load_extension("cogs")
accord.run(get_var('DISCORD_TOKEN'))
