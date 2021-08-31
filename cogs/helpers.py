import os
from nextcord import TextChannel, Thread


def get_var(key: str):
    # Raise error on nonexistent environment variable
    if key in os.environ:
        return os.environ[key]
    raise RuntimeError(f'Missing configuration key {key}. Please check your build vars.')


async def add_thread_emoji(thread: Thread):
    thread_emoji = '🧵'

    # Check if the name already has the thread emoji
    if not thread.name.startswith(thread_emoji):
        await thread.edit(name='{0}{1}'.format(thread_emoji, thread.name))


async def lock_channel(channel: TextChannel):
    # Check if already locked
    everyone = channel.guild.default_role
    existing_perms = channel.permissions_for(everyone)
    if existing_perms.send_messages_in_threads and not existing_perms.send_messages:
        return

    # Only allow @everyone to message threads, not text channels
    perms = channel.overwrites_for(everyone)
    perms.send_messages = False
    perms.send_messages_in_threads = True
    await channel.set_permissions(everyone, overwrite=perms)
