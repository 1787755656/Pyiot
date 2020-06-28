# -*- coding: UTF-8 -*-


class Event:
    def __init__(self, data):
        if "FromUin" in data.keys():  # 私聊消息
            self.send_to_type = 1
            self.user = data["FromUin"]
        elif "FromGroupId" in data.keys():
            self.send_to_type = 2
            self.user = data["FromGroupId"]
