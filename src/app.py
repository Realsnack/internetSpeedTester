import configparser
import json
import logging
import time

import testing

def main():
    config = loadConfig("src/config.json")
    logName = config["LogName"] + ".log"
    logging.basicConfig(filename=logName, filemode="w+", level=logging.DEBUG)

    logging.info("Program started, config loaded")

    sleepTime = config["SleepTime"]
    logging.info('Sleeptime set to %s', sleepTime)
    
    # while 1:
    #     testing.testInternetSpeed()
    #     time.sleep(sleepTime)

    testing.testInternetSpeed()

def loadConfig(configName):
    config = configparser.ConfigParser()

    with open(configName, "r") as f:
        config = json.load(f)

    return config


main()