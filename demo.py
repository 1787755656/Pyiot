# -*- coding: UTF-8 -*-

# ！！！！！！！！！！！！！！！！！！！！！
# 在开始前请确保你已经在iotqq上登陆了该账号
# ！！！！！！！！！！！！！！！！！！！！！

from pyiot import pyiot

# 启动pyiot
# 参数分别为：
# 要监听的URL（就是CoreConf.conf填写的那个）
# 机器人QQ号
# 日志等级（未完善，暂时填pyiot.DEBUG即可）
pi = pyiot.start("http://127.0.0.1:8888", "这里替换为你机器人的QQ号", pyiot.DEBUG)

# 设置前缀（只有开头是这个的消息才能触发命令，不支持正则表达式）
pi.prefix = "."

# 定义一个正则表达式
re = r"(echo|print|复读|输出)"


@pi.on_group_command(re)  # 设为群命令（支持正则）
@pi.on_friend_command(re)  # 设为私聊命令（支持正则）
def a(event):  # 这个函数突然不知道该取啥名，就随便取了一个
    print(event.main_text)
    # event.main_text是发送的文字去除前缀和命令剩下的文本
    text = event.main_text.strip()
    if event.msg_from_type == 2:
        # at_user 传入一个QQ号，在发送消息时at该QQ
        pi.send_message(" " + text, event, at_user=event.from_user_qq)
    else:
        pi.send_message(text, event)

# ---------------------------------------------------------------------
# 给你的机器人发送：“.print Pyiot is a Python framework based on IOTQQ.”
# 注意别漏了“.”，这是你设置的prefix
# 不出意外的话，他会@你并发送：Pyiot is a Python framework based on IOTQQ.
# ---------------------------------------------------------------------

