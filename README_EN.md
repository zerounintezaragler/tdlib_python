# Tdlib Python

** Tdlib python ** A library to make bot / userbot / anything related to telegram

- 🇮🇩 [Indonesia] (./ readme.md)
- 🇺🇸 [English] (./ readme_en.md)
- 🇰🇷 [Korea, Republic of South Korea] (./ readme_ko.md)
- 🇨🇳 [China] (./ readme_zh-cn.md)
- 🇿🇦 [South Africa] (./ readme_af.md)
- 🇮🇳 [India] (./ readme_hi.md)
- 🇯🇵 [Japan] (./ readme_ja.md)
- 🇷🇺 [russia] (./ readme_ru.md)
- 🇹🇭 [Thailand] (./ readme_th.md)
- 🇦🇪 [United Arab Emirates] (./Readme_ar.md)


## Fact

- This library is not bound by many dependencies 3

## Feature

- [x] ** Very fast ** Ashnc library
- [x] ** Easy to use **

## Example

- [simple example] (https://github.com/zerounintezaragler/tdlib_python/tree/main/quickstart)



## Install

Before installing make sure you know Basic Python at least you have installed Ptyhon on your computer / device. [Python website] (https://www.python.org)

- ** Python **

  `` `Bash
  Pip Install Tdlib-Python
  `` `

## Documentation

### ensureineinealized

The method must be called freely want to be after ** on ** / before the method ** on ** but I suggest before ** on **

**example:**

`` `Python
  Tdlibpythonzerounintezaragler.ensureinitialized (librarypath = "fork/dependencies/lib/libtdlib_python.so")
`` `

### Initialized

This method must be called after the ** on ** method because to process updates

**example:**

`` `Python
  Await Tdlibpythonzerounintezaragler.initialized ()
`` `

### On

This method is useful for getting data updates from invokes / updates

**example:**

`` `Python

  def on_callback (update: dict):
    print (update)

  Tdlibpythonzerounintezaragler.on (event_name = "update", on_callback = on_callback)
  
`` `


### CreateClient

To create a new client, make sure you call the method.

**example:**

`` `Python
Newclientid = Tdlibpythonzerounintezaragler.CreateClient ()
print (newclientid)
`` `


### Invoke

To call the API you need to read the documentation directly

- [url docs] (other_url_docs) is easy to read for the public 

Here I only provide Parameters Data Map, Map / Json There are several important keys


| Key | Description | Value | MUST FILLED |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| **@type ** | This is filling with the method of | ** String ** | ** Yes ** |
| **@client_id ** | It contains client ID from the ** CreateClient ** Method ** | ** Int ** | ** if for the sync method there must be something that is not ** |
| **@extra ** | Fill in the Unique ID because the ASYNC method does not return directly data so it needs extra as a key return data | ** String ** | ** No ** |


If we have filled the mandatory parameters, we continue how to invoke the fire

- ** Setlogveribilitylevel **
  because this is the log method, you use the sync method 
  and not required to fill in the key **@client_id **

  example: 


`` `Python
  Tdlibpythonzerounintezaragler.invokesync (Parameters = {
    "@type": "Setlogverability",
    "New_VeverBosity_Level": 0,
  });
`` `

- ** Sendmessage **
  To send messages using this library, make sure the client is logged in
  [Reference documentation of Sendmessage] (URL DOCS)

`` `Python

        /// Take from createclient or update
        client_id = 1;
        getme = await tdlibpythonzerounintezaragler.invoke (parameters = {
          "@type": "getme",
          "@client_id": client_id,
        });
        print (getme);
        Await Tdlibpythonzerounintezaragler.invoke (Parameters = {{
          "@type": "Sendmessage",
          "@client_id": CliEnt_ID,
          "chat_id": getme ["id"],
          "Type": "text",
          "Text": "Hello",
        });
`` `

On top of that is just an example, to use another method, just fill in the parameters data, make sure the key parameters must be filled according to the table, I mean there are some key that must be filled, otherwise it will send data errors



## Help

**Difficult**? I have built ** library ** this ** as well as possible ** maybe and ** try easy ** to read and ** used as best as possible **. 

if ** you ** still ** feel ** ** difficulty ** and ** confusion ** ** try to join ** to ** group ** we in ** free without any cost **

- [telegram] (https://t.me/developer_global_public)

** Before joining ** Make sure ** use profile ** that ** clear ** we don't mind who you are, and any rank, but ** Make sure ** ** there is a username and photo profile **, and try to ** chat in the group ** ** no personal chat ** because it ** general group and maybe other people are confused **. If ** does not follow ** this is the possibility ** Cannot access chat in the group and will be banned **, the solution to use the second account, because after being banned we cannot respond quickly


## Support Me

If you feel this program is useful, you can support me [github zerounintezaragler] (https://github.com/zerounintezaragler) on the link is available social media and my sponsors. I don't mind if you only follow / donate a little money

[] (https://github.com/zerounintezaragler/zerounintezaragler/blob/main/asses/gopay.png)

- https://github.com/sponsors/zerounintezaragler

Thank You


Zerounintezaragler-18-07-2025


## Tags

- tdlib_python python