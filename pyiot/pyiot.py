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
                self.logger.info("接收", "收到群组消息")
                self.logger.debug(message)
                __on_message("group", message)

            @sio.on('OnFriendMsgs')
            def on_friend_msgs(message):
                """ 监听好友消息 """
                self.logger.info("接收", "收到好友消息")
                self.logger.debug(message)
                __on_message("friend", message)

            def __on_message(msg_type, message):
                message_content = message["CurrentPacket"]["Data"]["Content"]
                if msg_type == "friend":
                    command_dict = self.command_friend_dict
                    msg_type_num = 1
                elif msg_type == "group":
                    command_dict = self.command_group_dict
                    msg_type_num = 2
                else:
                    raise ValueError('type must be "friend" or "group"')
                for key, value in command_dict.items():
                    if message_content[:len(self.prefix)] == self.prefix:
                        message_content_no_prefix = message_content.lstrip(self.prefix)
                        if re.match(key, message_content_no_prefix):
                            value(event.Event(message, msg_type_num, self.prefix + key if self.prefix else key))

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
            self.logger.debug("框架事件", f"将{func.__name__}注册为好友命令的回调函数，命令为：{c}", "注册")
            return func

        return decorate

    def on_group_command(self, c):
        def decorate(func):
            self.command_group_dict[c] = func
            self.logger.debug("框架事件", "将{func.__name__}注册为群聊命令的回调函数，命令为：{c}", "注册")
            return func

        return decorate

    def reply(self, content, eve, at_user=0):
        if isinstance(content, str):
            data = {
                # 如果是群聊的话，用群号，其它（好友和私聊）用QQ号
                "toUser": eve.from_group_id if eve.msg_from_type == 2 else eve.from_user_qq,
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
            self.logger.debug("接收", "响应内容：", response.content)
