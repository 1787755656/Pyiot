# API文档

## 装饰器
* `@pi.on_friend_command(str)`  
传入一个正则表达式，当好友消息成功匹配到该正则时调用被装饰函数  
示例：`@pi.on_friend_command("(你好|hello)")`
* `@pi.on_group_command(str)`  
传入一个正则表达式，当群聊消息成功匹配到该正则时调用被装饰函数    
示例：`@pi.on_group_command("(你好|hello)")`

## 函数
* `pi.set_prefix(str)`  
设置命令前缀