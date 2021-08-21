from discord import Client


class AccordClient(Client):
    async def on_ready(self):
        # Hello, world
        print('Logged on as {0}!'.format(self.user))
