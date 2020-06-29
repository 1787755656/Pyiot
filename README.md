# Pyiot
一个基于IOTQQ的Python框架。  
  
## 开发文档
  
### 快速上手
**请查看[demo.py](https://www.github.com/KongChengPro/Pyiot/tree/master/demo.py)**
### API
#### 装饰器
* `@pi.on_friend_command(str)`  
传入一个正则表达式，当好友消息成功匹配到该正则时调用被装饰函数  
示例：`@pi.on_friend_command("(你好|hello)")`
* `@pi.on_group_command(str)`  
传入一个正则表达式，当群聊消息成功匹配到该正则时调用被装饰函数    
示例：`@pi.on_group_command("(你好|hello)")`

#### 函数  
* `pi.send_message(self, content, eve, at_user=0)`
发送消息

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
