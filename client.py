from discord import Client


class AccordClient(Client):
    async def on_ready(self):
        # Hello, world
        print('Logged on as {0}!'.format(self.user))

    async def on_thread_join(self, thread):
        # Thread created, check if the name has the thread emoji
        thread_emoji = "🧵"

        if thread_emoji not in thread.name:
            await thread.edit(name='{0}{1}'.format(thread_emoji, thread.name))
