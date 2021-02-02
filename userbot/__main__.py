# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot
from userbot.modules import ALL_MODULES


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("You are running Project Fizilion")

LOGS.info(
    "Congratulations, your userbot is now running !! Test it by typing .alive / .on in any chat."
    "If you need assistance, head to https://t.me/ProjectFizilion")

btlg = os.environ.get("BOTLOG") or "False"

if btlg:
    api = os.environ.get("API_KEY")
    _hash = os.environ.get("API_HASH")
    cid = os.environ.get("BOTLOG_CHATID")
    with TelegramClient(StringSession(), api, _hash) as client:
        msg = "Master, Fizilion is now alive, \nTest it by typing .alive in the chat"
        client.send_message(cid, msg)
    
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
