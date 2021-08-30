import pyrebase
from .loop import AccordLoop
from .commands import AccordCommands
from .helpers import get_var
from nextcord.ext.commands import Bot


def setup(bot: Bot):
    # Instantiate Pyrebase
    print('Logging into Firebase')
    firebase = pyrebase.initialize_app({
        'apiKey': get_var('FIREBASE_KEY'),
        'authDomain': get_var('FIREBASE_AUTH_DOMAIN'),
        'databaseURL': get_var('FIREBASE_DB_URL'),
        'storageBucket': get_var('FIREBASE_BUCKET'),
        'serviceAccount': {
            'client_email': get_var('FIREBASE_CLIENT_EMAIL'),
            'client_id': get_var('FIREBASE_CLIENT_ID'),
            'private_key': get_var('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
            'private_key_id': get_var('FIREBASE_PRIVATE_KEY_ID'),
            'type': 'service_account'
        },
    })
    db = firebase.database()

    # Add cogs
    print('Adding cogs')
    bot.add_cog(AccordLoop(bot))
    bot.add_cog(AccordCommands(bot, db))
