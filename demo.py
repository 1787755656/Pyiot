# -*- coding: UTF-8 -*-

from pyiot import pyiot

# 参数分别为：
# 要监听的URL（就是CoreConf.conf填写的那个）
# 机器人QQ号
# 日志等级（未完善）
pi = pyiot.start("http://127.0.0.1:8888", "机器人的QQ号", pyiot.DEBUG)


# 将这个函数注册为一个命令，当一条消息能够被装饰器传入的参数匹配时触发该函数（支持正则表达式）
# 同一个函数可以使用多个装饰器来注册
@pi.on_friend_command("(阿伟死了|awsl)")  # 当一条私聊消息以 阿伟死了 或 awsl 开头时触发
@pi.on_group_command("awsl")  # 当一条群聊消息以 awsl 开头时触发
def awsl(event):
    pi.reply("阿伟：我没死！", event)  # 快捷回复，传入event，将消息发送给event所指向的群或好友
