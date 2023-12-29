from Fronius.Fronius import Get_Fronius_Data

temp = Get_Fronius_Data(["http://192.168.0.36/solar_api/v1/GetPowerFlowRealtimeData.fcgi"])
print(temp)