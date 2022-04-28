import tinytuya as tt
import json
import time
import random

def main():
    fileName = 'local_keys.json'
    lights = setBulbs(fileName)
    retry = False
    while('Error' in lights[0].set_colour(lights[0].coulor_rgb()).keys()):
        aquireDeviceInfo()
        if retry:
            raise KeyError("Somethings wrong with your keys") 
        retry = True

        time.sleep(1)

def aquireDeviceInfo():
    file = open('local_keys.json')
    localKeys = json.load(file)
    allDevices = tt.deviceScan()
    for device in allDevices:
        for count in range(len(localKeys)):
            if(localKeys[count]['ip'] == device['ip'] ):
                localKeys[count]['id'] = device['gwID']
            elif(localKeys[count]['id'] == device['gwID']):
                localKeys[count]['ip'] == device['ip']

def setBulbs(filename):
    file = open(filename)
    localKeys = json.load(file)
    bulbs = []
    for count,item in enumerate(localKeys):
        bulb = tt.BulbDevice(item["id"], item["ip"], item["key"], dev_type='default')
        bulb.set_version(3.3)
        bulbs.append(bulb)
    return bulbs
    

main()