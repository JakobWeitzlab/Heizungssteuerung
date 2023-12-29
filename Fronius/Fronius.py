import json
import requests

def Get_Fronius_Data(urls, searchKeys):
    values = []
    for url in urls:
        try:
            apiResponse = requests.get(url, timeout=5)
            apiResponseJson = json.loads(str(apiResponse.text))

            #Grab apropriate value
            if isinstance(searchKeys, list):
                for sk in searchKeys:
                    values.append(Get_Values_From_Response(sk, apiResponseJson))
            else:
                values.append(Get_Values_From_Response(searchKeys, apiResponseJson))

            #ActualPower = apiResponseJson["Body"]["Data"]["Inverters"]["1"]["P"]
            #DayPower = apiResponseJson["Body"]["Data"]["Inverters"]["1"]["E_Day"]

            return values
        except requests.exceptions.Timeout:
            print("Wechselrichter: ", url, "ist offline")
            
def Get_Values_From_Response(searchKeys, inputDic):
    if searchKeys in inputDic:
        return inputDic[searchKeys]

    for v in inputDic.values():
        if isinstance(v, dict):
            found = Get_Values_From_Response(searchKeys, v)
            if found is not None:
                return found
    return None

