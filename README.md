# Pyiot
一个基于IOTQQ的Python框架。  
* [Pyiot](#pyiot)
  * [开发文档](#开发文档)
      * [请注意](#请注意)
    * [快速上手 / DEMO](#快速上手--demo)
  * [更新日志](#更新日志)
    * [2020/6/29](#2020629)
    * [2020/6/30](#2020630)
  * [更新计划](#更新计划)
    * [API](#api)
      * [Pyiot](#pyiot-1)
      * [装饰器](#装饰器)
      * [函数](#函数)
  * [特别鸣谢](#特别鸣谢)

## 开发文档
#### 请注意
* 该框架暂不支持发送和接收私聊消息（即没有好友，通过群聊等方式发起会话）

### 快速上手 / DEMO
（如果在demo中发现bug，请通过邮箱联系我3136106883@qq.com，感谢）
1. 第一个机器人：[first_bot.py](https://www.github.com/KongChengPro/Pyiot/tree/master/demo_first_bot.py)
2. 聊天机器人：[smart_bot.py](https://www.github.com/KongChengPro/Pyiot/tree/master/demo_smart_bot.py)
## 更新日志
### 2020/6/29: 
* 将send_message方法更改为reply
* prefix现在支持正则
### 2020/6/30
* 优化接口命名
> `reply` -> `msg_reply`
* 新增`bot_open`, `bot_close`, `bot_status`方法
* 增加了一个智能聊天机器人的demo
* 增加了一个实例化Pyiot的的可选参数`socketio_logger`
* 在`__init__.py`中加入了一个`get_pyiot`函数，现在可以使用如下方式启动pyiot
```
import pyiot

pi = pyiot.get_pyiot("http://127.0.0.1:8888", "机器人QQ号", log_level="DEBUG", socketio_logger=False)
pi.start()
```
## 更新计划
- [ ] 提供message_builder类，用于构建一条消息，使用send方法发送
### API
#### Pyiot
使用如下方式启动pyiot
```
import pyiot

pi = pyiot.get_pyiot("http://127.0.0.1:8888", "机器人QQ号", log_level="DEBUG", socketio_logger=False)
pi.start()
```
#### 装饰器
* `@pi.on_friend_command(str)`  
传入一个正则表达式，当好友消息成功匹配到该正则时调用被装饰函数  
示例：`@pi.on_friend_command("(你好|hello)")`
* `@pi.on_group_command(str)`  
传入一个正则表达式，当群聊消息成功匹配到该正则时调用被装饰函数    
示例：`@pi.on_group_command("(你好|hello)")`

#### 函数  
* `pi.msg_reply(self, content, eve, at_user=0)`
发送消息，依次传入：消息内容，event，要at的QQ
* `pi.bot_close`, `pi.bot_open`, `pi.bot_status`
依次为：关闭机器人，打开机器人，获取机器人状态（关闭返回False，打开返回True）
## 特别鸣谢
（排名不分先后）  
[IOTQQ](https://github.com/IOTQQ/IOTQQ)
：Pyiot的诞生离不开IOTQQ的支持  
[Pycharm](https://www.jetbrains.com/pycharm/)
：Pycharm大大加快了Pyiot的开发进度  
[Python](https://www.python.org/)
：这个强大而优雅的语言使得Pyiot成为可能  
[IOTQQ涩图插件](https://github.com/yuban10703/IOTQQ-color_pic/)
：让我不用重复写解析json的代码（用了他写好的，节省体力【滑稽】）  
[青云客](http://www.qingyunke.com/)
：为`smart_bot`一章提供了API
