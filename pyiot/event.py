# -*- coding: UTF-8 -*-


class Event:
    def __init__(self, message, msg_from_type, command=""):
        # msg_type: 1 好友，2 群聊， 3 私聊
        self.msg_from_type = msg_from_type
        self.msg_type = message['CurrentPacket']['Data']['MsgType']
        if self.msg_from_type == 2:
            self.current_qq = message['CurrentQQ']  # 接收到这条消息的QQ
            self.from_group_id = message['CurrentPacket']['Data']['FromGroupId']  # 来源QQ群
            self.from_group_name = message['CurrentPacket']['Data']['FromGroupName']  # 来源QQ群名称
            self.from_user_qq = message['CurrentPacket']['Data']['FromUserId']  # 哪个QQ发过来的
            self.from_user_name = message['CurrentPacket']['Data']['FromNickName']  # 来源QQ的群名片
            self.msg_seq = message['CurrentPacket']['Data']['MsgSeq']  # 序列
            self.msg_random = message['CurrentPacket']['Data']['MsgRandom']
            self.content = message['CurrentPacket']['Data']['Content']
        elif self.msg_from_type == 1:
            self.current_qq = message['CurrentQQ']  # 接收到这条消息的QQ
            self.to_user_qq = message['CurrentPacket']['Data']['ToUin']  # 接收到这条消息的QQ（和上面的区别未知）
            self.from_user_qq = message['CurrentPacket']['Data']['FromUin']  # 来源QQ
            self.content = message['CurrentPacket']['Data']['Content']  # 消息内容
        self.main_text = self.content.lstrip(command)
