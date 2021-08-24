import os
from utils import AccordClient


def get_var(key: str):
    if key in os.environ:
        return os.environ[key]
    raise RuntimeError(f'Missing configuration key {key}. Please check your build vars.')


accord = AccordClient()
accord.run(get_var('DISCORD_TOKEN'))
