import speedtest
import logging
from datetime import datetime
from os import path
from elasticclient import ElasticClient


class Testing:
    def __init__(self, csvName, elasticHosts):
        self.csvName = csvName
        self.es = ElasticClient(elasticHosts)

    def testPing(self):
        logging.critical('Ping not implemented')

    def saveIntoCsv(self, upSpeed, downSpeed):
        if path.exists(self.csvName):
            with open(self.csvName, 'a+') as f:
                f.write(datetime.now().strftime('%H:%M:%S %d.%m.%y') +
                        ';' + str(upSpeed/10) + ';' + str(downSpeed/10) + '\n')
                f.close()
        else:
            with open(self.csvName, 'w+') as f:
                f.write('DateTime;UpSpeed;DownSpeed\n')
                f.write(datetime.now().strftime('%H:%M:%S %d.%m.%y') +
                        ';' + str(upSpeed/10) + ';' + str(downSpeed/10) + '\n')
                f.close()

    def testInternetSpeed(self):
        speed = speedtest.Speedtest()
        logging.info('Testing download speed')
        downSpeed = speed.download()
        logging.debug('downSpeed ' + str(downSpeed))
        logging.info('Testing upload speed')
        upSpeed = speed.upload()
        logging.debug('upSpeed ' + str(upSpeed))

        downSpeed = int(downSpeed/100000)
        upSpeed = int(upSpeed/100000)

        if downSpeed <= 100:
            logging.warning(
                'Download speed is below 10Mbs: %s Mbs', downSpeed/10)
        else:
            logging.info('Download speed is: %s Mbs', downSpeed/10)

        if upSpeed <= 20:
            logging.warning('Upload speed is below 2Mbs: %s Mbs', upSpeed/10)
        else:
            logging.info('Upload speed is: %s Mbs', upSpeed/10)

        self.saveIntoCsv(upSpeed, downSpeed)
        self.logSpeedToElastic(upSpeed/10, downSpeed/10)

    def logSpeedToElastic(self, upSpeed, downSpeed):
        timestamp = datetime.now()
        logging.debug('Timestamp: %s', timestamp)
        self.es.index(timestamp, upSpeed, downSpeed)
