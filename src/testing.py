import speedtest
import logging

def testPing():
    print('ping')

def testInternetSpeed():
    speed = speedtest.Speedtest()
    downSpeed = speed.download()
    upSpeed = speed.upload()

    downSpeed = downSpeed/100000
    upSpeed = upSpeed/100000

    if downSpeed <= 100:
        logging.warning('Download speed is below 10Mbs: %s Mbs', downSpeed/10)
    else:
        logging.info('Download speed is: %s Mbs', downSpeed/10)

    if upSpeed <= 20:
        logging.warning('Upload speed is below 2Mbs: %s Mbs', upSpeed/10)
    else:
        logging.warning('Upload speed is: %s Mbs', upSpeed/10)