＃Tdlib Python

** tdlib python **库制作bot / userbot /与电报有关的任何内容

 - 🇮🇩[印度尼西亚]（./ readme.md）
 - 🇺🇸[英语]（./ readme_en.md）
 - 🇰🇷[韩国，韩国共和国]（./ readme_ko.md）
 - 🇨🇳[中国]（./ readme_zh-cn.md）
 - 🇿🇦[南非]（./ readme_af.md）
 - 🇮🇳[印度]（./ readme_hi.md）
 - 🇯🇵[日本]（./ readme_ja.md）
 - 🇷🇺[俄罗斯]（./ readme_ru.md）
 - 🇹🇭[泰国]（./ readme_th.md）
 - 🇦🇪[阿拉伯联合酋长国]（./readme_ar.md）


＃＃ 事实

 - 该库不受许多依赖关系的约束3

＃＃ 特征

 -  [x] **非常快** ashnc库
 -  [x] **易于使用**

＃＃ 例子

 -  [简单示例]（https://github.com/zerounintezaragler/tdlib_python/tree/main/main/quickstart）



＃＃ 安装

在安装之前，请确保您了解基本的Python，至少您已经在计算机 /设备上安装了Ptyhon。 [Python网站]（https://www.python.org）

- ** Python **

  ``bash
  PIP安装tdlib-python
  ````````

##文档

###确保我化

必须自由地称呼该方法在**之前** / **之前的**，但我建议在**上**之前**

**例子：**

``python
  tdlibpythonzerounintezaragler。
````````

###初始化

必须以**方法的**来调用此方法，因为要处理更新

**例子：**

``python
  等待tdlibpythonzerounintezaragler.Initialized（）
````````

＃＃＃ 在

此方法对于从invokes /更新获取数据更新很有用

**例子：**

``python

  def on_callback（更新：dict）：
    打印（更新）

  tdlibpythonzerounintezaragler.on（event_name =“ update”，on_callback = on_callback）
  
````````


### createClient

要创建一个新客户，请确保调用该方法。

**例子：**

``python
newClientId = tdlibpythonzerounintezaragler.createclient（）
打印（newClientID）
````````


### Invoke

要拨打API，您需要直接阅读文档

 -  [url docs]（其他_url_docs）很容易阅读公众 

在这里，我仅提供参数数据图，地图 / json有几个重要的键


|键|描述|值|必须填写|
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| **@type ** |这是用|的方法填充的**字符串** | **是** |
| **@client_id ** |它包含来自** createClient **方法** |的客户端ID。 ** int ** | **如果用于同步方法，则必须没有** |
| **@extra ** |填写唯一ID，因为异步方法没有直接返回数据，因此需要额外作为键返回数据| **字符串** | **否** |


如果我们填写了强制性参数，我们将继续如何调用火

 -  ** setLogibilitylevel **
  因为这是日志方法，所以您使用同步方法 
  并且不需要填写密钥**@client_id **

  例子： 


``python
  tdlibpythonzerounintezaragler.invokesync（parameters = {
    “ @Type”：“ setLogverability”，
    “ new_veverbosity_level”：0，
  }）;
````````

 -  ** sendmessage **
  要使用此库发送消息，请确保客户端已登录
  [sendmessage的参考文档]（URL文档）

``python

        ///从CreateClient或更新
        client_id = 1;
        getme =等待tdlibpythonzerounintezaragler.invoke（parameters = {
          “ @Type”：“ GetMe”，
          “ @client_id”：client_id，
        }）;
        打印（getme）;
        等待tdlibpythonzerounintezaragler.invoke（parameters = {{{
          “ @Type”：“ sendmessage”，
          “ @client_id”：CLIent_id，
          “ chat_id”：getme [“ id”]，
          “ type”：“ text”，
          “文字”：“你好”，
        }）;
````````

最重要的只是一个示例，使用另一种方法，只需填写参数数据，请确保必须根据表填充关键参数



＃＃ 帮助

**难的**？我已经建立了**库**这个**，也许**可能会尝试阅读和**尽可能多地使用** **。 

如果**您**仍然**感觉** **困难**和**混乱** **尝试加入**与**组**我们无需任何费用**

 -  [Telegram]（https://t.me/developer_global_public）

**加入** **请确保使用个人资料** **清晰**我们不介意您是谁，任何等级，但是** ** ** ** ** **有一个用户名和照片配置文件**，然后尝试**在组中**聊天** **没有个人聊天** ** ** **，因为它**是**一般组和其他人和其他人感到困惑**。如果**不遵循**这是可能性**无法访问组中的聊天，并且将被禁止**，这是使用第二个帐户的解决方案，因为被禁止后，我们无法快速响应


##支持我

如果您认为此程序很有用，则可以支持我[Github Zerounintezaragler]（https://github.com/zerounintezaragler），可提供社交媒体和我的赞助商。我不介意您是否只关注 /捐赠一点钱

[]（https://github.com/zerounintezaragler/zerounintezaragler/blob/main/main/asses/gopay.png）

-https：//github.com/sponsors/zerounintezaragler

谢谢


Zerounintezaragler-18-07-2025


##标签

-tdlib_python python