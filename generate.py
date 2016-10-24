from random import randint
from time import sleep

from core import PRODUCER, PRODUCER_TOPIC

if __name__ == '__main__':
    print('Generate started')
    for _ in range(1000):
        number = randint(0, 100000)
        PRODUCER.send(PRODUCER_TOPIC, number)
        print('Number sent {}'.format(number))
        sleep(0.010) #sleep 10 ms
