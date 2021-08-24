from discord import Thread


async def add_thread_emoji(thread: Thread):
    thread_emoji = "🧵"

    # Check if the name already has the thread emoji
    if not thread.name.startswith(thread_emoji):
        await thread.edit(name='{0}{1}'.format(thread_emoji, thread.name))
