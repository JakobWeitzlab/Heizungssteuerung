# import Libraries
import websockets
import asyncio
import logging

from main import DataPresentFromWeb

class WebSocket:
    def ProcessMessages(self,input):

        getRequest = []
        for index, v in enumerate(input):
            if(v=="GET"):
                getRequest.append(input[index+1])
        return getRequest
    
    async def Handler(self,websocket):
        self.getRequest = []
        incomingMessages = []

        async for message in websocket:
            incomingMessages = message.split(',')
            getRequest = self.ProcessMessages(incomingMessages)
            
            #Retreive Data from Fronius
            FroniusResponse = DataPresentFromWeb(getRequest, demo=False)
            FroniusResponseString = ",".join(map(str,FroniusResponse))

            #Send Requested Data
            print(FroniusResponseString)
            await websocket.send(FroniusResponseString)

            
    async def StartWebSocket(self):
        #stop = asyncio.Future()
        logging.basicConfig(level=logging.DEBUG)
        server = await websockets.serve(self.Handler, host="", port=8765, )

        #await stop
        #await server.close()
        print("WebSocket server started...")
