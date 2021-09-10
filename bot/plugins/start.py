# © its-leo-bitch
from os import environ
from bot import bot
from pyrogram import filters, types
from bot.config import Config

BOTUSERNAME = Config.BOTUSERNAME

@bot.on_message(filters.command('start'))
async def start_handle(client, message):
    if len(message.text.split()) >= 2:
        if message.text.split()[1] == 'help_inline':
            await message.reply(
                f"""**How to use <b>@{BOTUSERNAME}</b> via inline\n\n type in `<b>@{BOTUSERNAME}</b>` <language> <code>**\n\n See /langs for loaded languages\n\n **A Project of;\n @WONKRU_HERE**""",
                reply_markup=types.InlineKeyboardMarkup(
                    [
                        [
                            types.InlineKeyboardButton(
                                'Example',
                                switch_inline_query_current_chat='python print("Hello World")'
                            )
                        ]
                    ]
                )
            )
    else:
        await message.reply(
            f"""**Usage**\n
`/eval` or `/eval [language]` if you want to go for a quick code execution.\n\n
Executing files are not supported yet but will in future\n\n
you can also use me via inline:\n`<b>@{BOTUSERNAME}</b> python3 print('Hello World')`\n\n
all available languages can be seen on `/langs`\n\n
**A Project of; @WONKRU_HERE**"""
   )
