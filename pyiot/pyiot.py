# -*- coding: utf-8 -*-
import json
import re
import threading

import requests
import socketio

from pyiot import event
from pyiot import simple_logger


class Pyiot:
    def __init__(self, host, qq, log_level="INFO", socketio_logger=False):
        self.socketio_logger = socketio_logger
        self.logger = simple_logger.SimpleLogger()
        self.logger.set_level(log_level)
        self.host = host
        self.qq = qq
        self.command_friend_dict = {}
        self.command_group_dict = {}
        self.prefix = ""
        self.bot_status = False

    def start(self):
        """ 启动Pyiot """

        def _():
            sio = socketio.Client(logger=self.socketio_logger)

            @sio.event
            def connect():
                """ 连接 """
                sio.emit('GetWebConn', self.qq)  # 取得当前已经登录的QQ链接

            @sio.on('OnGroupMsgs')
            def on_group_msgs(message):
                """ 监听群组消息 """
                __on_message("group", message)

            @sio.on('OnFriendMsgs')
            def on_friend_msgs(message):
                """ 监听好友消息 """
                __on_message("friend", message)

            def __on_message(msg_type, message):
                if self.bot_status:
                    return
                message_content = message["CurrentPacket"]["Data"]["Content"]
                if msg_type == "friend":
                    self.logger.info("接收", "收到好友消息")
                    self.logger.debug(message)
                    command_dict = self.command_friend_dict
                    msg_type_num = 1
                    from_user_qq = message["CurrentPacket"]["Data"]["FromUin"]
                elif msg_type == "group":
                    self.logger.info("接收", "收到群组消息")
                    self.logger.debug(message)
                    command_dict = self.command_group_dict
                    msg_type_num = 2
                    from_user_qq = message["CurrentPacket"]["Data"]["FromUserId"]
                else:
                    raise ValueError("Param `msg_type` must be `friend` or `group` (not {})".format(msg_type))
                if str(from_user_qq) == str(self.qq):
                    return
                for key, value in command_dict.items():
                    cmd = self.prefix + key if self.prefix else key
                    if re.match(cmd, message_content):
                        self.logger.info("框架事件", "收到了", message_content, "前往调用", value.__name__)
                        value(event.Event(message, msg_type_num, cmd))

            @sio.on('OnEvents')
            def on_events(message):
                """ 监听事件 """
                self.logger.debug("接收", message)

            sio.connect(self.host, transports=['websocket'])
            self.logger.info("框架事件", f"成功连接到{self.host}")
            sio.wait()
            sio.disconnect()

        self.logger.info("框架事件", f"Pyiot已启动")
        thread = threading.Thread(target=_)
        thread.setName("Thread - Listen for events")
        thread.start()

    def on_friend_command(self, c):
        def decorate(func):
            self.command_friend_dict[c] = func
            self.logger.debug("框架事件", "将{}注册为好友命令的回调函数，命令为：{}".format(func.__name__, c))
            return func

        return decorate

    def on_group_command(self, c):
        def decorate(func):
            self.command_group_dict[c] = func
            self.logger.debug("框架事件", "将{}注册为群命令的回调函数，命令为：{}".format(func.__name__, c))
            return func

        return decorate

    def msg_reply(self, content, eve, at_user=0):
        if isinstance(content, str):
            to_qq = eve.from_group_id if eve.msg_from_type == 2 else eve.from_user_qq
            data = {
                # 群聊用群号，好友用QQ号
                "toUser": to_qq,
                "sendToType": eve.msg_from_type,
                "sendMsgType": "TextMsg",
                "content": content,
                "groupid": 0,
                "atUser": at_user,
                "replayInfo": None
            }
            self.logger.info("发送", "向{}发送了{}".format(data["toUser"], data["content"]))
            headers = {'Content-Type': 'application/json'}
            url = self.host + "v1/LuaApiCaller" if self.host[-1] == "/" else self.host + "/v1/LuaApiCaller"
            params = {
                "qq": self.qq,
                "funcname": "SendMsg",
                "timeout": 19
            }
            response = requests.post(url=url, headers=headers, data=json.dumps(data), params=params)
        else:
            raise ValueError("Param `content` must be a str (not {})".format(type(content)))

    def bot_open(self):
        self.bot_status = False

    def bot_close(self):
        self.bot_status = False

    def bot_get_status(self):
        return self.bot_status
