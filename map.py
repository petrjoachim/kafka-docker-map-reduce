from time import sleep
from core import PRODUCER, PRODUCER_TOPIC, CONSUMER

if __name__ == '__main__':
    print("Map started")
    for message in CONSUMER:
        print('Got message {}'.format(message.value))
        sleep(1.000)
        PRODUCER.send(PRODUCER_TOPIC, message.value)