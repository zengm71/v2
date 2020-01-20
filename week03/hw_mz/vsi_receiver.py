import paho.mqtt.client as mqtt
from cv2 import imdecode, IMREAD_COLOR, imwrite
import numpy as np
LOCAL_MQTT_HOST="mqtt_broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="homework3"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	

def on_message_local(client, userdata, msg):
  try:
    print("message received locally!")	    
    png_new = imdecode(np.fromstring(msg.payload, dtype=np.uint8),IMREAD_COLOR)
    imwrite('/home/debug_new.png', png_new)
    print('==============================')
    # if we wanted to re-publish this message, something like this should work
    # msg = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message_local

local_mqttclient.loop_forever()