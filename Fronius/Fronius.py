import json
import requests
import logging
#import traceback

def Get_Fronius_Data(urls, searchKeys):
    values = []
    for url in urls:
        try:
            apiResponse = requests.get(url, timeout=5)
            apiResponseJson = json.loads(str(apiResponse.text))

            #Grab apropriate value
            if isinstance(searchKeys, list):
                for sk in searchKeys:
                    values.append(str(sk)+","+str(Get_Values_From_Response(sk, apiResponseJson)))
            else:
                values.append(str(searchKeys)+","+str(Get_Values_From_Response(searchKeys, apiResponseJson)))

            return values
    
        except requests.exceptions.Timeout:
            print("Wechselrichter: ", url, "ist offline")
            startIndex = url.find('://')
            endIndex = url.find('/', startIndex+3)
            address = url[startIndex+3:endIndex]
            pass
        except Exception as e:
            logging.error(e)
            
def Get_Values_From_Response(searchKeys, inputDic):
    if searchKeys in inputDic:
        return inputDic[searchKeys]

    for v in inputDic.values():
        if isinstance(v, dict):
            found = Get_Values_From_Response(searchKeys, v)
            if found is not None:
                return found
    return None

demo = False
if demo:
    temp = Get_Fronius_Data(["http://192.168.0.36/solar_api/v1/GetPowerFlowRealtimeData.fcgi", "http://192.168.0.36/solar_api/v1/GetPowerFlowRealtimeData.fcgi"],["E_Day","P"])
    print(temp)