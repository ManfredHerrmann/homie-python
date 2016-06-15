#!/usr/bin/env python
import time
import homie
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

switchNode = homie.HomieNode("switch", "switch")


def switchOnHandler(mqttc, obj, msg):
    payload = msg.payload.decode("UTF-8").lower()
    if payload == 'true':
        logger.info("Switch: ON")
    else:
        logger.info("Switch: OFF")


def main():
    Homie = homie.Homie(**homie.config)
    Homie.setFirmware("relay-switch", "1.0.0")
    Homie.subscribe(switchNode, "on", switchOnHandler)

    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logger.warn("Quitting.")
