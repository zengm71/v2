# Homework 3

## On Jetson

1. Create a bridge network
`docker network create --driver bridge hw03`

2. MQTT broker

    * Build the image

        `sudo docker build -t mqtt_broker -f dockerfile_tx2_mqtt_broker .`

    * Spin up container and establish broker

        `sudo docker run --rm --name mqtt_broker --network hw03 -p 1883:1883 -ti mqtt_broker /usr/sbin/mosquitto`

3. MQTT forwarder

    * Build the image

        `sudo docker build -t mqtt_forwarder -f dockerfile_tx2_mqtt_forwarder .`

    * Spin up container and run `tx2_forwarder.py`

        `sudo docker run --rm --name mqtt_forwarder --network hw03 -v ~/Documents/W251/v2/week03/hw_mz/:/home/ -ti mqtt_forwarder /bin/sh /home/tx2_run_forwarder.sh`

4. OpenCV face detector

    * Build the image

        `sudo docker build -t face_detector -f dockerfile_tx2_face_detector .`

    * Spin up the container and run `tx2_face_detector.py`

        `sudo docker run --rm --privileged -e DISPLAY --name face_detector --network hw03 -v ~/Documents/W251/v2/week03/hw_mz/:/home/ -ti face_detector /bin/bash /home/tx2_run_face_detector.sh`

## On VSI

1. Create a bridge network
`sudo docker network create --driver bridge hw03`

2. MQTT broker

    * Build the image

        `sudo docker build -t mqtt_broker -f dockerfile_vsi_mqtt_broker .`

    * Spin up container and establish broker

        `sudo docker run --rm --name mqtt_broker --network hw03 -p 1883:1883 -ti mqtt_broker /usr/sbin/mosquitto`

3. MQTT receiver

    * Build the image

        `sudo docker build -t mqtt_receiver -f dockerfile_vsi_mqtt_receiver .`

    * Spin up container and run `vsi_receiver.py`

        `sudo docker run --rm --name mqtt_receiver --network hw03 -v ~/W251/HW/hw03/:/home/ -ti mqtt_receiver /bin/bash /home/vsi_run_receiver.sh`