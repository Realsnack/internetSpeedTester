import configparser
import json
import logging


def main():
    config = loadConfig("src/config.json")
    logName = config["LogName"] + ".log"
    logging.basicConfig(filename=logName, filemode="w+", level=logging.DEBUG)

    logging.info("Program started, config loaded")

    sleepTime = config["SleepTime"]
    logging.info('Sleeptime set to %s', sleepTime)

    while 1:
        print('lol')


def loadConfig(configName):
    config = configparser.ConfigParser()

    with open(configName, "r") as f:
        config = json.load(f)

    return config


main()