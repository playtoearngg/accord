from .loop import AccordLoop
from nextcord.ext.commands import Bot


def setup(bot: Bot):
    print('Adding cogs')
    bot.add_cog(AccordLoop(bot))
