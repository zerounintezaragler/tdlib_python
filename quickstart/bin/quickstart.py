import asyncio
import os
import sys

tdlib_python_package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../package/tdlib_python/lib'))
sys.path.append(tdlib_python_package_path)

from tdlib_python import *


async def main():


    print("start")

    tdlibPythonZerounIntezarAgler = TdlibPythonZerounIntezarAgler()
    
    tdlibPythonZerounIntezarAgler.ensureInitialized(libraryPath="path_to_library/libtdlib_python.so")

    def on_callback(update:dict):
        print(update)
    tdlibPythonZerounIntezarAgler.on(event_name="update", on_callback=on_callback)

    # debug
    # tdlibPythonZerounIntezarAgler.emit(event_name="update", value={
    #     "@type": "ok",
    # });

    await tdlibPythonZerounIntezarAgler.initialized();
    result = tdlibPythonZerounIntezarAgler.invoke(parameters={
        "@type": "getMe",
    });
    print(result) 

    print("done")


asyncio.run(main())


