# -*- coding: UTF-8 -*-

from pyiot import pyiot

pi = pyiot.start("http://127.0.0.1:8888", "机器人的QQ号", pyiot.DEBUG)


@pi.on_friend_text_command("(阿伟死了|awsl)")
@pi.on_group_text_command("awsl")
def awsl(event):
    pi.reply("阿伟：我没死！", event)