# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-

from pyiot import pyiot

pi = pyiot.Pyiot("http://127.0.0.1:8888", "机器人QQ", log_level="INFO", socketio_logger=False)
pi.prefix = ""

# 设置管理员列表（仅管理员可以使用 打开/关闭/查询状态 的命令）
pi.admins = [123456789]
pi.bot_command_open = ".开启"  # 设置 打开机器人 的命令
pi.bot_command_close = ".关闭"  # 设置 关闭机器人 的命令
pi.bot_command_status = ".状态"  # 设置 查询机器人状态 的命令

pi.start()


# 写一个命令测试一下关了之后还能不能回复（不能）
@pi.on_friend_command(r"\?")  # 注意，这里是正则匹配，而"?"是正则表达式中的关键字，需要用反斜杠转义才能正常使用
@pi.on_group_command(r"\?")
def test(event):
    pi.msg_reply("你发送的是：" + event.main_text, event)
