from time import sleep
from core import PRODUCER, PRODUCER_TOPIC, CONSUMER

if __name__ == '__main__':
    print("Reduce started")
    total = 0
    count = 0
    for message in CONSUMER:
        total += message.value
        count += 1

        print("Actual average {}".format(total / count))