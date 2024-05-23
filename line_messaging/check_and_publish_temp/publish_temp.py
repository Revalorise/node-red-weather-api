import paho.mqtt.client as paho
from get_temp import get_temp


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to broker')
    else:
        print('Connection failed')


def on_publish(client, userdata, result):
    print(f'{result} has been published.')


client = paho.Client(protocol=paho.MQTTv311)
client.on_connect = on_connect
client.on_publish = on_publish

client.connect('broker.hivemq.com', 1883)
client.loop_start()

try:
    # Get temperature and classify it if necessary
    temperature = get_temp()

    # Publish the temperature to the MQTT topic
    result = client.publish('weather_data/temperature', temperature, qos=1)
    result.wait_for_publish()
    status = result[0]

    if status == 0:
        print(f'Successfully sent temperature: {temperature}')
    else:
        print(f'Failed to send message with temperature: {temperature}')

    client.loop_stop()
    client.disconnect()

except KeyboardInterrupt:
    print("Exiting loop")
