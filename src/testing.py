import speedtest
import logging

def testPing():
    logging.critical('Ping not implemented')

def testInternetSpeed():
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
        logging.warning('Download speed is below 10Mbs: %s Mbs', downSpeed/10)
    else:
        logging.info('Download speed is: %s Mbs', downSpeed/10)

    if upSpeed <= 20:
        logging.warning('Upload speed is below 2Mbs: %s Mbs', upSpeed/10)
    else:
        logging.info('Upload speed is: %s Mbs', upSpeed/10)