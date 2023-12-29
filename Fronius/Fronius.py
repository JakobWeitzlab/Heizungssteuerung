import json
import requests

#urls = ["http://192.168.0.36/solar_api/v1/GetPowerFlowRealtimeData.fcgi"]
def Get_Fronius_Data(urls):

    for url in urls:
        apiResponse = requests.get(url)
        apiResponseJson = json.loads(str(apiResponse.text))

        #Grab apropriate value
        ActualPower = apiResponseJson["Body"]["Data"]["Inverters"]["1"]["P"]
        DayPower = apiResponseJson["Body"]["Data"]["Inverters"]["1"]["E_Day"]

        return ActualPower, DayPower
        #print(DayPower, ActualPower)