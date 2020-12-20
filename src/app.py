import configparser
import json
import logging
import time

import testing


def main():
    config = loadConfig("src/config.json")
    logName = config["LogName"] + ".log"
    logging.basicConfig(filename=logName, filemode="w+", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.info("Program started, config loaded")

    sleepTime = int(config["SleepTime"])
    logging.info("Sleeptime set to %s", sleepTime)

    while 1:
        logging.info("Testing Ping")
        testing.testPing()
        logging.info("Testing Speed")
        testing.testInternetSpeed()
        logging.info("Sleeping for %ss", sleepTime)
        time.sleep(sleepTime)
        logging.info("Sleeping done")


def loadConfig(configName):
    config = configparser.ConfigParser()

    with open(configName, "r") as f:
        config = json.load(f)

    return config


main()