# -*- coding: UTF-8 -*-

import random
import urllib.parse

import requests

import pyiot

pi = pyiot.get_pyiot("http://127.0.0.1:8888", "机器人的QQ号", log_level="DEBUG", socketio_logger=False)
pi.start()  # 启动pyiot
pi.prefix = r""  # 将前缀设为空字符串，即任何时候都可以匹配


@pi.on_group_command("")  # 将命令设为空字符串，即任何时候都可以匹配
def chat(event):
    # 每条消息有1/10的几率会被回复（做成时不时出来插一句嘴活跃气氛的效果）
    if random.randint(1, 10) == 1:
        # 感谢青云客提供的免费聊天机器人API
        url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(event.main_text))
        result = requests.get(url)
        content = result.json()["content"]
        msg = content.replace("{br}", "\n")
        pi.msg_reply(msg, event)
