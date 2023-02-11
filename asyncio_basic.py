import asyncio


async def other():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return "返回值"


async def func():
    print("执行协程函数内部代码")
    response = await other()
    print(response)


asyncio.run(func())

# 短视频开发
