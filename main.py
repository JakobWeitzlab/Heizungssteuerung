#Import Libraries
import schedule
import time
import asyncio

#Import functions
from Fronius.Fronius import Get_Fronius_Data


def DataPresentFromWeb(input, demo):
    print("fetching")
    urlsFronius = ['http://192.168.0.36/solar_api/v1/GetPowerFlowRealtimeData.fcgi', 'http://192.168.0.7/solar_api/v1/GetPowerFlowRealtimeData.fcgi']
    response = []

    #Demo Mode if Fronius is offline
    if demo:
        return ["9999"]
    
    if input:
        response = Get_Fronius_Data(urlsFronius, input)
        return response

async def Schedule_Tasks():
    while True:
        await asyncio.sleep(1)

async def main():
    from Websocket.websocket import WebSocket
    ws = WebSocket()
    await asyncio.gather(ws.StartWebSocket(), Schedule_Tasks())

    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except:
        loop.close()
    