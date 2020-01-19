import numpy as np
import cv2
import paho.mqtt.client as mqtt
import time


# start MQTT client ================================================================================
LOCAL_MQTT_HOST="mqtt_broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="homework3"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client, userdata, msg):
  try:
    print("message received!")	
    # if we wanted to re-publish this message, something like this should work
    # msg = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# start capturing faces ============================================================================
# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
face_cascade = cv2.CascadeClassifier('/home/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)

i = 0
while(True):
  i += 1
  print(i)
  
  local_mqttclient.publish(LOCAL_MQTT_TOPIC, payload = i, qos = 0, retain = False)
  time.sleep(10)

  # # Capture frame-by-frame
  # ret, frame = cap.read()

  # # We don't use the color information, so might as well save space
  # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # # face detection and other logic goes here
  # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  # for (x,y,w,h) in faces:
  #     # your logic goes here; for instance
      
  #     # cut out face from the frame.. 
  #     face = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
      
  #     # we can save the png just to see if it worked: cv2.imwrite('/home/test.png', face)
      
  #     # encode the image
  #     rc,png = cv2.imencode('.png', face)
  #     msg = png.tobytes()

  #     # send it to broker
  #     local_mqttclient.publish(LOCAL_MQTT_TOPIC, payload = msg, qos = 0, retain = False)
