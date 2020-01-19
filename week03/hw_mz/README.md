# On Jetson

1. Create a bridge network
`docker network create --driver bridge hw03`

2. MQTT broker

    * Build the image

        `sudo docker build -t mqtt_broker -f dockerfile_tx2_mqtt_broker .`

    * Spin up container and establish broker

        `sudo docker run --name mqtt_broker --network hw03 -p 1883:1883 -ti mqtt_broker /usr/sbin/mosquitto`

3. MQTT forwarder

    * Build the image

        `sudo docker build -t mqtt_fowarder -f dockerfile_tx2_mqtt_forwarder .`

    * Spin up container

        `sudo docker run --name mqtt_fowarder --network hw03 -p 1883:1883 -ti mqtt_fowarder`

    * Subscribe to topic `homework3`

        `mosquitto_sub -h mqtt_broker -t homework3`

4. OpenCV face detector

    * Build the image

        `sudo docker build -t face_detector -f dockerfile_tx2_face_detector .`

    * Spin up the container and run `tx2_face_detector.py`

        `sudo docker run --rm --privileged -e DISPLAY --name face_detector --network hw03 -v ~/Documents/W251/v2/week03/hw_mz/:/home/ -ti face_detector tx2_face_detector.py`