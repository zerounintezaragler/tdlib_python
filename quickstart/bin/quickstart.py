import asyncio
import os
import sys
import time

tdlib_python_package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../package/tdlib_python/lib'))
sys.path.append(tdlib_python_package_path)

from tdlib_python import *

def ask(text: str) -> str:
    while True:
        print()
        user_input = input(f"{text}?: ")
        if user_input is not None and user_input.strip():
            return user_input.strip()

async def main():


    print("start")

    tdlibPythonZerounIntezarAgler = TdlibPythonZerounIntezarAgler()
    
    # tdlibPythonZerounIntezarAgler.ensureInitialized(libraryPath="path_to_library/libtdlib_python.so")
    tdlibPythonZerounIntezarAgler.ensureInitialized(libraryPath="/home/galaxeus/Documents/github/azkadev/telegram_client/package/tdlib_library/linux/lib/libtelegram.so")

    tdlibPythonZerounIntezarAgler.invokeSync(parameters={
        "@type": "setLogVerbosityLevel",
        "new_verbosity_level": 0,
    })

    async def on_callbackAsync(update:dict):
        client_id = update.get("@client_id")
        if isinstance(client_id, int):
            client_id = client_id
        elif client_id is None or not isinstance(client_id, int):
            client_id = 0
        
        if client_id<1:
           return
        
        if update["@type"] == "updateAuthorizationState":
            authorization_state = update.get("authorization_state", {})

            if authorization_state["@type"] == "authorizationStateWaitTdlibParameters":
                telegramApiId = ask(text="Telegram Api Id");
                telegramApiHash = ask(text= "Telegram Api Hash");
                await tdlibPythonZerounIntezarAgler.invoke(parameters={
                  "@type": "getAuthorizationState",
                  "@client_id": newTdlibClientId,
                })

    def on_callback(update:dict):
        asyncio.run(on_callbackAsync(update=update))
 
    tdlibPythonZerounIntezarAgler.on(event_name="update", on_callback=on_callback)

    # debug
    # tdlibPythonZerounIntezarAgler.emit(event_name="update", value={
    #     "@type": "ok",
    # });

    await tdlibPythonZerounIntezarAgler.initialized();

    newTdlibClientId = tdlibPythonZerounIntezarAgler.createClient()

    await tdlibPythonZerounIntezarAgler.invoke(parameters={
       "@type": "getAuthorizationState",
       "@client_id": newTdlibClientId,
    })
    
    print("done")
    

    while True:
      time.sleep(1 / 1000.0)



asyncio.run(main())


