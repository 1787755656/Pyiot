# -*- coding: UTF-8 -*-

# ！！！！！！！！！！！！！！！！！！！！！
# 在开始前请确保你已经在iotqq上登陆了该账号
# ！！！！！！！！！！！！！！！！！！！！！

from pyiot import pyiot
import time
# 实例化pyiot
# 参数分别为：
# 要监听的URL（就是CoreConf.conf填写的那个）
# 机器人QQ号
# 日志等级，可选择["DEBUG", "INFO", "WARNING", "ERROR", "FATAL"]其一
# socketio日志，为False则不输出，为True则输出
pi = pyiot.Pyiot("http://127.0.0.1:8888", "你机器人的QQ", log_level="INFO", socketio_logger=False)
pi.start()  # 启动pyiot

# 设置前缀（只有开头是这个的消息才能触发命令，不支持正则表达式）
pi.prefix = "."

# 我们先来写一个最基础的命令

# 定义一个正则表达式
re = r"(echo|print|输出)"


@pi.on_group_command(re)  # 设为群命令（支持正则）
@pi.on_friend_command(re)  # 设为私聊命令（支持正则）
def a(event):  # 这个函数突然不知道该取啥名，就随便取了一个
    print(event.main_text)
    # event.main_text是发送的文字去除前缀和命令剩下的文本
    text = event.main_text.strip()
    if event.msg_from_type == 2:
        # at_user 传入一个QQ号，在发送消息时at该QQ
        pi.reply(" " + text, event, at_user=event.from_user_qq)
    else:
        pi.reply(text, event)

# ---------------------------------------------------------------------
# 给你的机器人发送：“.print Pyiot is a Python framework based on IOTQQ.”
# 注意别漏了“.”，这是你设置的prefix
# 不出意外的话，他会发送（如果在群聊中使用会at使用者）：Pyiot is a Python framework based on IOTQQ.
# ---------------------------------------------------------------------


# 接下来写一个可以指定复读次数的命令（这里注释就不写那么多了，自己看代码吧，挺简单的）
@pi.on_group_command(r"(rp|repeat|重复)")
@pi.on_friend_command(r"(rp|repeat|重复)")
def b(event):  # 这个函数突然不知道该取啥名，就随便取了一个
    # event.main_text是发送的文字去除前缀和命令剩下的文本
    try:
        num = int(event.main_text[0])
    except ValueError:
        pi.reply("ERROR: rp后必须跟着一个阿拉伯数字", event)
        # 你可以使用pyiot自带的logger记录log（第一个参数是Tag，第二个是正文）
        # logger共有五个等级["DEBUG", "INFO", "WARNING", "ERROR", "FATAL"]
        pi.logger.warning("demo", "有用户尝试输入一个非法数字")
        return
    for i in range(int(num)):
        pi.reply(event.main_text[1:], event)
        time.sleep(1)

# ---------------------------------------------------------------------
# 试试给机器人发送：“.rp5Hello, World!”吧~
# ---------------------------------------------------------------------
