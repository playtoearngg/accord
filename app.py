import os
from utils import AccordClient
from utils.loop import AccordLoop


def get_var(key: str):
    # Raise error on nonexistent environment variable
    if key in os.environ:
        return os.environ[key]
    raise RuntimeError(f'Missing configuration key {key}. Please check your build vars.')


# Instantiate Discord client
accord = AccordClient(command_prefix='a.')
accord_loop = AccordLoop(accord)
accord.run(get_var('DISCORD_TOKEN'))
