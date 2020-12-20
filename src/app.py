from datetime import datetime
import configparser
import json
import logging
import time
import os

import testing


def main():
    config = loadConfig("config.json")
    logDateTime = datetime.now().strftime('%d_%m_%y')
    logName = config['LogName'] + logDateTime + ".log"
    csvName = config['CsvName'] + logDateTime + '.csv'

    try:
        os.mkdir('log')
    except OSError:
        print("Creation of the directory %s failed" % 'log')
    else:
        print("Successfully created the directory %s " % 'log')

    try:
        os.mkdir('csv')
    except OSError:
        print("Creation of the directory %s failed" % 'csv')
    else:
        print("Successfully created the directory %s " % 'csv')

    logging.basicConfig(filename=logName, filemode="w+",
                        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.info("Program started, config loaded")

    sleepTime = int(config["SleepTime"])
    logging.info("Sleeptime set to %s", sleepTime)

    try:
        while 1:
            runTest(sleepTime, csvName)
    except:
        logging.exception('An error occured')


def loadConfig(configName):
    config = configparser.ConfigParser()

    with open(configName, "r") as f:
        config = json.load(f)

    return config


def runTest(sleepTime, csvName):
    logging.info("Testing Ping")
    testing.testPing()
    logging.info("Testing Speed")
    testing.testInternetSpeed(csvName)
    logging.info("Sleeping for %ss", sleepTime)
    time.sleep(sleepTime)
    logging.info("Sleeping done")


main()
