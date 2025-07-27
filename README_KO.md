# tdlib 파이썬

** tdlib python ** 봇 / userbot / Telegram과 관련된 모든 것을 만들기위한 라이브러리

- [인도네시아] (./ readme.md)
- [영어] (./ readme_en.md)
- republic [한국, 한국 공화국] (./ readme_ko.md)
-. [중국] (./ readme_zh-cn.md)
-] [남아프리카] (./ readme_af.md)
-. [인도] (./ readme_hi.md)
-. [일본] (./ readme_ja.md)
- [러시아] (./ readme_ru.md)
-] [태국] (./ readme_th.md)
- [아랍 에미리트 연합] (./readme_ar.md)


## 사실

-이 라이브러리는 많은 종속성에 구속되지 않습니다 3

## 특징

- [x] ** 매우 빠른 ** ASHNC 라이브러리
- [x] ** 사용하기 쉬움 **

## 예

- [간단한 예] (https://github.com/zerounintezaragler/tdlib_python/tree/main/quickstart)



## 설치하다

설치하기 전에 최소한 컴퓨터 / 장치에 Ptyhon을 설치 한 기본 Python을 알고 있어야합니다. [Python 웹 사이트] (https://www.python.org)

- ** 파이썬 **

  ```Bash
  pip tdlib-python을 설치하십시오
  ```

## 문서

### 보장

이 방법은 ** On ** 이전 ** 전에 ** / on ** on ** on ** on **를 제안합니다.

**예:**

```Python
  tdlibpythonzerounintezaragler.ensureinitialized (librarypath = "포크/의존성/lib/libtdlib_python.so")
```

### 초기화

이 방법은 ** on ** 메소드 후에 호출되어야합니다.

**예:**

```Python
  Tdlibpythonzerounintezaragler.initialized ()를 기다립니다.
```

### 에

이 방법은 호출 / 업데이트에서 데이터 업데이트를 얻는 데 유용합니다.

**예:**

```Python

  def on_callback (업데이트 : dict) :
    인쇄 (업데이트)

  tdlibpythonzerounintezaragler.on (event_name = "update", on_callback = on_callback)
  
```


### createclient

새 클라이언트를 만들려면 메소드를 호출하십시오.

**예:**

```Python
newClientID = tdlibpythonzerounintezaragler.createclient ()
인쇄 (NewClientID)
```


### 부르다

API를 호출하려면 문서를 직접 읽어야합니다.

- [URL DOCS] (Other_URL_DOCS)는 대중을 위해 쉽게 읽을 수 있습니다. 

여기서는 매개 변수 데이터 맵, Map / JSON 만 제공합니다. 몇 가지 중요한 키가 있습니다.


| 키 | 설명 | 가치 | 채워 져야 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| **@type ** | 이것은 |의 방법으로 채워진다 ** 문자열 ** | ** 예 ** |
| **@client_id ** | ** CreateClient ** Method **의 클라이언트 ID가 포함되어 있습니다. ** int ** | ** 동기화 메소드의 경우 **가 아닌 것이 있어야합니다 |
| **@extra ** | Async 메소드가 직접 데이터를 반환하지 않으므로 주요 반환 데이터로 추가가 필요하기 때문에 고유 ID를 채우십시오 | ** 문자열 ** | ** 아니요 ** |


필수 매개 변수를 채우면 불을 부르는 방법을 계속합니다.

- ** setLogVeriblyLevel **
  로그 메소드이므로 Sync 메소드를 사용합니다. 
  키 **@client_id **를 채울 필요가 없습니다.

  예: 


```Python
  tdlibpythonzerounintezaragler.invokesync (매개 변수 = {
    "@type": "setLogVerability",
    "new_veverbosity_level": 0,
  });
```

- ** SendMessage **
  이 라이브러리를 사용하여 메시지를 보내려면 클라이언트가 로그인했는지 확인하십시오.
  [SendMessage의 참조 문서] (URL 문서)

```Python

        /// CreateClient에서 가져 오거나 업데이트하십시오
        client_id = 1;
        getme = Await tdlibpythonzerounintezaragler.invoke (매개 변수 = {
          "@type": "getme",
          "@client_id": client_id,
        });
        인쇄 (getme);
        tdlibpythonzerounintezaragler.invoke를 기다리고 있습니다 (매개 변수 = {{
          "@type": "sendmessage",
          "@client_id": CLIENT_ID,
          "chat_id": getme [ "id"],
          "유형": "텍스트",
          "텍스트": "안녕하세요",
        });
```

그 외에도 다른 방법을 사용하려면 매개 변수 데이터를 채우고 테이블에 따라 주요 매개 변수를 채워야하는지 확인하십시오. 채워야 할 키가 있다는 것을 의미합니다. 그렇지 않으면 데이터 오류를 보냅니다.



## 돕다

**어려운**? 나는 ** 라이브러리 **이 **를 만들었습니다. 

만약 ** 당신이 ** 여전히 ** 느낌 ** ** 난이도 ** 및 ** 혼란 ** ** ** ** 그룹 **에 가입하려고 ** 우리는 ** 비용없이 ** 무료 **

- [전보] (https://t.me/developer_global_public)

**에 가입하기 전에 ** 분명한 **를 사용하십시오 ** 명확한 ** 우리는 당신이 누구인지, 어떤 계급도 신경 쓰지 않지만 ** ** 사용자 이름과 사진 프로필 **가 있는지 확인하십시오 ** 그룹에서 ** 개인 채팅 ** 일반 그룹과 다른 사람들이 혼란을 겪기 때문에 ** 개인 채팅 ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** 개인 채팅 **. **가 따르지 않는 경우 ** 이것은 가능성입니다 **는 그룹의 채팅에 액세스 할 수 없으며 금지 될 것입니다 **, 두 번째 계정을 사용하는 솔루션입니다. 금지 된 후에는 신속하게 응답 할 수 없기 때문입니다.


## 나를 지원합니다

이 프로그램이 유용하다고 생각되면 링크에서 [github zerounintezaragler] (https://github.com/zerounintezaragler)를 지원할 수 있습니다. 당신이 약간의 돈을 팔로우 / 기부해도 괜찮습니다.

[] (https://github.com/zerounintezaragler/zerounintezaragler/blob/main/asses/gopay.png)

-https://github.com/sponsors/zerounintezaragler

감사합니다


Zerounintezaragler-18-07-2025


## 태그

-tdlib_python python