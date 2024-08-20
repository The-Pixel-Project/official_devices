#!/usr/bin/env python
#
# Python code which automatically posts Message in a Telegram Group if any new update is found.
# Intended to be run on every push
# USAGE : python3 post.py
# See README for more.
#
# Copyright (C) 2024 PrajjuS <theprajjus@gmail.com>
#
# Credits: Ashwin DS <astroashwin@outlook.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import telebot
import os
import json
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
from NoobStuffs.libtelegraph import TelegraphHelper

# Get configs from workflow secrets
def getConfig(config_name: str):
    return os.getenv(config_name)
try:
    BOT_TOKEN = getConfig("BOT_TOKEN")
    CHAT_ID = getConfig("CHAT_ID")
    PRIV_CHAT_ID = getConfig("PRIV_CHAT_ID")
    PIXELPROJECT_VERSION_CHECK = getConfig("PIXELPROJECT_VERSION_CHECK")
except KeyError:
    print("Fill all the configs plox..\nExiting...")
    exit(0)

BANNER_PATH = "./banners/t.png"

# Init bot
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
telegraph = TelegraphHelper(
    author_name="The Pixel Project Bot",
    author_url="https://t.me/pixelproject_bot",
    domain="graph.org"
)

# File directories
jsonDir = "OTA/devices"
idDir = ".github/scripts"

# Store IDs in a file to compare
def update(IDs):
    with open(f"{idDir}/file_ids.txt", "w+") as log:
        for ids in IDs:
            log.write(f"{str(ids)}\n")

# Return IDs of all latest files from json files
def get_new_id():
    files = []
    file_id = []
    for all in os.listdir(jsonDir):
        if all.endswith('.json'):
            files.append(all)
    for all_files in files:
        with open(f"{jsonDir}/{all_files}", "r") as file:
            data = json.loads(file.read())['response'][0]
            file_id.append(data['md5'])
    return file_id

# Return previous IDs
def get_old_id():
    old_id = []
    with open(f"{idDir}/file_ids.txt", "r") as log:
        for ids in log.readlines():
            old_id.append(ids.replace("\n", ""))
    return old_id

# Remove elements in 2nd list from 1st, helps to find out which device got an update
def get_diff(new_id, old_id):
    first_set = set(new_id)
    sec_set = set(old_id)
    return list(first_set - sec_set)

# Grab needed info using ID of the file
def get_info(ID):
    files = []
    for all in os.listdir(jsonDir):
        if all.endswith('.json'):
            files.append(all)
    for all_files in files:
        with open(f"{jsonDir}/{all_files}", "r") as file:
            data = json.loads(file.read())['response'][0]
            if data['md5'] == ID:
                device = all_files
                break
    with open(f"{jsonDir}/{device}") as device_file:
        info = json.loads(device_file.read())['response'][0]
        PIXELPROJECT_VERSION = info['version']
        OEM = info['oem']
        DEVICE_NAME = info['device']
        DEVICE_CODENAME = device.split('.')[0]
        MAINTAINER = info['maintainer']
        DATE_TIME = datetime.datetime.fromtimestamp(int(info['timestamp']))
        DOWNLOAD_URL = info['download']
        SIZE = round(int(info['size'])/1000000000, 2)
        MD5 = info['md5']
        SHA256 = info['sha256']
        XDA = info['forum']
        TELEGRAM = info['telegram']
        msg = ""
        msg += f"The Pixel Project {PIXELPROJECT_VERSION}\n"
        msg += f"Device Name: {OEM} {DEVICE_NAME} ({DEVICE_CODENAME})\n"
        msg += f"Maintainer: {MAINTAINER}\n"
        msg += f"Date Time: {DATE_TIME}\n"
        # msg += f"Download URL: {DOWNLOAD_URL}\n"
        msg += f"Size: {SIZE}G\n"
        msg += f"MD5: {MD5}\n"
        msg += f"SHA256: {SHA256}\n"
        msg += f"XDA: {XDA}\n"
        msg += f"Telegram: {TELEGRAM}\n\n"
        print(msg)
        return {
            "version": PIXELPROJECT_VERSION,
            "oem": OEM,
            "device_name": DEVICE_NAME,
            "codename": DEVICE_CODENAME,
            "maintainer": MAINTAINER,
            "datetime": DATE_TIME,
            "download": DOWNLOAD_URL,
            "size": SIZE,
            "md5": MD5,
            "sha256": SHA256,
            "xda": XDA,
            "telegram": TELEGRAM
        }

# Prepare function for posting message in channel
def send_post(chat_id, image, caption):
    return bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

# Prepare message format for channel
def message_content(information):
    msg = ""
    msg += f"➡️ New build available for <b>{information['oem']} {information['device_name']} ({information['codename']})</b>\n"
    msg += f"👤 by <a href='{information['telegram']}'>{information['maintainer']}</a>\n\n"
    msg += f"ℹ️ Version: <b>{information['version']}</b>\n"
    msg += f"📆 Build date: <b>{information['datetime']}</b>\n"
    msg += f"📂 Size: <b>{information['size']}GB</b>\n"
    msg += f"⬇️ <a href='{information['download']}'>Download now</a>\n\n"
    msg += f"💬 <a href='https://t.me/ThePixelProjectChat'>View discussion</a>"
    return msg

# Send updates to channel and commit changes in repo
def tg_message():
    commit_message = "Update new IDs and push OTA"
    commit_description = "Data for following device(s) were changed:\n"
    if len(get_diff(get_new_id(), get_old_id())) == 0:
        print("All are Updated\nNothing to do\nExiting...")
        sleep(2)
        exit(1)
    else:
        print(f"IDs Changed:\n{get_diff(get_new_id(), get_old_id())}\n\n")
        for devices in get_diff(get_new_id(), get_old_id()):
            info = get_info(devices)
            with open(BANNER_PATH, "rb") as image:
                send_post(CHAT_ID, image, message_content(info))
            commit_description += f"- {info['device_name']} ({info['codename']})\n"
            sleep(5)
    update(get_new_id())
    open("commit_mesg.txt", "w+").write(f"ThePixelProject: {commit_message} [BOT]\n\n{commit_description}")

# Prepare function for posting message in private group
def send_log(chat_id, text, button):
    return bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=button,
        disable_web_page_preview=True
    )

# Get all the devices which are in official repo
def get_devices():
    files = []
    devices = []
    for all in os.listdir(jsonDir):
        if all.endswith('.json'):
            files.append(all)
    for device in files:
        with open(f"{jsonDir}/{device}", "r") as file:
            data = json.loads(file.read())['response'][0]
            devices.append({
                "device_name": data['device'],
                "codename": device.split('.')[0],
                "maintainer": data['maintainer'],
                "telegram": data['telegram'],
                "version": data['version']
            })
    return devices

# Prepare log format for private group
def tg_log():
    Updated = []
    YetToUpdate = []
    buttons = InlineKeyboardMarkup()
    for device in get_devices():
        if device['version'] == PIXELPROJECT_VERSION_CHECK:
            Updated.append(device)
        else:
            YetToUpdate.append(device)
    count = 1
    msg = ""
    msg += f"<b>The Pixel Project Update Status</b><br><br>"
    msg += f"<b>The following devices have been updated to the version</b> <code>{PIXELPROJECT_VERSION_CHECK}</code> <b>in the current month:</b> "
    if len(Updated) == 0:
        msg += f"<code>None</code>"
    else:
        for device in Updated:
            msg += f"<br><b>{count}.</b> <code>{device['device_name']} ({device['codename']})</code> <b>-</b> <a href='{device['telegram']}'>{device['maintainer']}</a>"
            count += 1
    msg += "<br><br>"
    count = 1
    msg += f"<b>The following devices have not been updated to the version</b> <code>{PIXELPROJECT_VERSION_CHECK}</code> <b>in the current month:</b> "
    if len(YetToUpdate) == 0:
        msg += f"<code>None</code>"
    else:
        for device in YetToUpdate:
            msg += f"<br><b>{count}.</b> <code>{device['device_name']} ({device['codename']})</code> <b>-</b> <a href='{device['telegram']}'>{device['maintainer']}</a>"
            count += 1
    msg += "<br><br>"
    msg += f"<b>Total Official Devices:</b> <code>{str(len(get_devices()))}</code><br>"
    msg += f"<b>Updated during current month:</b> <code>{str(len(Updated))}</code><br>"
    msg += f"<b>Not Updated during current month:</b> <code>{str(len(YetToUpdate))}</code><br><br>"
    msg += f"<b>Information as on:</b> <code>{str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M'))} hours (UTC)</code>"
    text = f"<b>Pixel Project Devices (v{PIXELPROJECT_VERSION_CHECK}) Update Status</b>\n\n"
    text += f"<b>Total Official Devices:</b> <code>{str(len(get_devices()))}</code>\n"
    text += f"<b>Updated during current month:</b> <code>{str(len(Updated))}</code>\n"
    text += f"<b>Not Updated during current month:</b> <code>{str(len(YetToUpdate))}</code>\n"
    text += f"<b>Information as on:</b> <code>{str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M'))} hours (UTC)</code>"
    telegph_url = telegraph.create_page(title="Device Update Status", content=msg)
    button1 = InlineKeyboardButton("More Info", telegph_url['url'])
    buttons.add(button1)
    send_log(PRIV_CHAT_ID, text, buttons)

# Final stuffs
tg_message()
tg_log()
print("Successful")
sleep(2)