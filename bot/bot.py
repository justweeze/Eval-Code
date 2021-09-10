# © Its-leo-bitch
from os import environ
from os import path
from configparser import ConfigParser
from pyrogram import Client
from piston import Piston
from .utils import langs, lang_names
from .config import Config

piston = Piston()
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN


class bot(Client):
    def __init__(self, name):
        config_file = f"{name}.ini"
        config = ConfigParser()
        config.read(config_file)
        name = name.lower()
        plugins = {'root': path.join(__package__, 'plugins')}
       
        super().__init__(
            name,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            config_file=config_file,
            workers=16,
            plugins=plugins,
            workdir="./",
        )

    async def start(self):
        await super().start()
        print("bot started. Hi.")
        languages = ''
        j = 1
        for v in (await piston.versions()):
            if j == 4:
                languages += f'|{(v.language+"-"+(v.version or "")):<15}|\n'
                j = 0
            else:
                languages += f'|{(v.language+"-"+(v.version or "")):<15}'
            j += 1
            langs.append(v)
            lang_names.append(v.language)
        j += 1
        print('+===============================================================+')
        print('|                    Loaded Languages                           |')
        print('+=============+===============+================+===============+')
        print(languages)
        print('+===============+=============+===============+=================+')

        print("bot started. Hi.")

    async def stop(self, *args):
        await super().send_message(947138292, "Bot going offline")
        await super().stop()
        print("bot stopped. Bye.")
