import configparser
import json

def main():
    config = loadConfig('src/config.json')

    sleepTime = config['SleepTime']
    print(sleepTime)

def loadConfig(configName):
    config = configparser.ConfigParser()

    with open(configName, 'r') as f:
        config = json.load(f)

    return config

main()