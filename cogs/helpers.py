import os
from nextcord import Thread


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
