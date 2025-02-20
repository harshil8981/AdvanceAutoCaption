import asyncio
import importlib

from pyrogram import idle

import info
from body import ALL_MODULES


async def init(): 
    for all_module in ALL_MODULES:
        importlib.import_module("body" + all_module)
    LOGGER("body").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...)
    LOGGER("body").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥𝗞𝗜𝗟𝗟𝗘𝗥☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    LOGGER("body").info("𝗦𝗧𝗢𝗣 𝗠𝗥𝗞𝗜𝗟𝗟𝗘𝗥 🎻 𝗕𝗢𝗧..")


if name == "main":
    asyncio.get_event_loop().run_until_complete(init())
