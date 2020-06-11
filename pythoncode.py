import time
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "ox61h3" #replace the ORG ID
deviceType = "Smart_agriculture"#replace the Device type wi
deviceId = "motor"#replace Device ID
authMethod = "token"
authToken = "gu*tlqz@Z@9cEF5yDP" #Replace the authtoken

def myCommandCallback(cmd): # function for Callback
        print("Command received: %s" % cmd.data)
        if cmd.data['command']=='motoron':
                print("MOTOR ON IS RECEIVED")
                          
        elif cmd.data['command']=='motoroff':
                print("MOTOR OFF IS RECEIVED")
        '''
                
        if cmd.command == "setInterval":
                
                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: 'interval'")
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: 'message'")
                else:
                        output=cmd.data['message']
                        print(output)
        '''
        data = {"Command" : cmd.data['command']}
        success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        
        myCommandCallback.has_been_called = True

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        
        '''
        T=50;
        H=32;
        ot=45
        
        data = {'d':{ 'Temperature' : Status, 'Humidity': H,'objTemp':ot }}
        #Send Temperature & Humidity to IBM Watson
        '''
        myCommandCallback.has_been_called = False
        
        Status = "Sensor is On"
        #cmd.data['command'] = "Rest"
        #Send Status to IBM Watson
        
        data= {'Status' : Status}
        #data2 = {'Command RECEIVED' : cmd.data['command'] }
        #print data
        def myOnPublishCallback():
            print (data, "to IBM Watson")
            #print (data2, "to IBM Watson")
        
        success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback
        if myCommandCallback.has_been_called == True :
            print("call made")
        
        
# Disconnect the device and application from the cloud
#deviceCli.disconnect()