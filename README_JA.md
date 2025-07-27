＃TDLIB Python

** tdlib python ** bot / userbot / telegramに関連するものを作るライブラリ

-🇮🇩[インドネシア]（./ readme.md）
-🇺🇸[英語]（./ readme_en.md）
-🇰🇷[韓国、韓国共和国]（./ readme_ko.md）
-🇨🇳[中国]（./ readme_zh-cn.md）
-🇿🇦[南アフリカ]（./ readme_af.md）
-🇮🇳[インド]（./ readme_hi.md）
-🇯🇵[日本]（./ readme_ja.md）
-🇷🇺[ロシア]（./ readme_ru.md）
-🇹🇭[タイ]（./ readme_th.md）
 - 🇦🇪[アラブ首長国連邦]（./readme_ar.md）


＃＃ 事実

 - このライブラリは多くの依存関係に縛られていません3

＃＃ 特徴

 -  [x] **非常に速い** ASHNCライブラリ
 -  [x] **使いやすい**

＃＃ 例

 -  [簡単な例]（https://github.com/zerounintezaragler/tdlib_python/tree/main/quickstart）



＃＃ インストール

インストールする前に、少なくともコンピューター /デバイスにPtyhonをインストールしていることを確認してください。 [Python Webサイト]（https://www.python.org）

 -  ** python **

  「バッシュ
  ピップインストールtdlib-python
  `` `

##ドキュメント

### suresinealized

メソッドは自由に呼ばれなければなりません** on ** / method ** on **の後に** / **が** on **を提案します**

**例：**

`` python
  tdlibpythonzerounintezaragler.ensureInitialized（librarypath = "fork/dependencies/lib/libtdlib_python.so"））
`` `

###初期化

この方法は、更新を処理するために** on **メソッドの後に呼び出す必要があります

**例：**

`` python
  待っているtdlibpythonzerounintezaragler.initialized（）
`` `

＃＃＃ の上

この方法は、Invoke / Updatesからデータの更新を取得するのに役立ちます

**例：**

`` python

  def on_callback（update：dict）：
    印刷（更新）

  tdlibpythonzerounintezaragler.on（event_name = "update"、on_callback = on_callback）
  
`` `


### CreateClient

新しいクライアントを作成するには、メソッドを呼び出すようにしてください。

**例：**

`` python
newClientId = tdlibpythonzerounintezaragler.createclient（）
print（newClientID）
`` `


###呼び出し

APIを呼び出すには、ドキュメントを直接読む必要があります

 -  [url docs]（other_url_docs）が一般に読みやすいです 

ここでは、パラメータデータマップのみを提供します。マップ / jsonいくつかの重要なキーがあります


|キー|説明|値|満たさなければならない|
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| **@タイプ** |これは、|の方法で満たされています**文字列** | **はい** |
| **@client_id ** | ** createclient ** method **のクライアントIDが含まれています| ** int ** | **同期メソッドの場合は、**ではないものがなければなりません|
| **@extra ** | Asyncメソッドが直接データを返さないため、キーリターンデータとして追加が必要なため、一意のIDを入力してください| **文字列** | **いいえ** |


必須のパラメーターを埋めた場合、火災を呼び出す方法を続けます

 -  ** setLogverivivileLevel **
  これはログメソッドであるため、同期メソッドを使用します 
  キーに記入する必要はありません**@client_id **

  例： 


`` python
  tdlibpythonzerounintezaragler.invokesync（parameters = {{
    「@Type」：「SetLogverability」、
    「New_Veverbosity_Level」：0
  }）;
`` `

 -  ** sendmessage **
  このライブラリを使用してメッセージを送信するには、クライアントがログインしていることを確認してください
  [sendmessageの参照ドキュメント]（url docs）

`` python

        /// createClientまたは更新から取得します
        client_id = 1;
        getme = await tdlibpythonzerounintezaragler.invoke（parameters = {
          「@Type」：「GetMe」、
          「@client_id」：client_id、
        }）;
        print（getMe）;
        待っているtdlibpythonzerounintezaragler.invoke（parameters = {{{{
          「@type」：「sendmessage」、
          「@client_id」：client_id、
          「chat_id」：getme ["id"]、
          「タイプ」：「テキスト」、
          「テキスト」：「こんにちは」、
        }）;
`` `

その上に、別のメソッドを使用し、パラメーターデータを入力するだけで、キーパラメーターがテーブルに従って入力する必要があることを確認するための単なる例です。



＃＃ ヘルプ

**難しい**？私は**ライブラリ**を作成しました**可能な限り**たぶん**簡単に試してみてください**読み取り、**可能な限り使用されます**。 

if ** you ** still ** feel ** **難易度**と**混乱** ** **から**グループ**私たちは**無料で無料** ** ** **

 -  [Telegram]（https://t.me/developer_global_public）

** **確認する前に**プロフィールを使用します**その**クリア**私たちはあなたが誰であるか、そして** ** **ユーザー名と写真プロファイル**があることを確認してください** ** ** **一般的なグループと他の人が混乱しているからです。 **に従わない場合**これは可能性**グループ内のチャットにアクセスできず、禁止されます** 2番目のアカウントを使用するソリューション、禁止された後、迅速に応答できないため


##私をサポートします

このプログラムが便利だと思う場合は、リンクで私をサポートできます[github zerounintezaragler]（https://github.com/zerounintezaragler）は、ソーシャルメディアと私のスポンサーを利用できます。あなたがちょっとしたお金だけをフォロー /寄付するかどうかは気にしません

[]（https://github.com/zerounintezaragler/zerounintezaragler/blob/main/asses/gopay.png）

-https：//github.com/spons/zerounintezaragler

ありがとう


Zerounintezaragler-18-07-2025


##タグ

-tdlib_python python