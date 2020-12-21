from elasticsearch import Elasticsearch
from datetime import datetime
import logging


class ElasticClient:
    def __init__(self, elasticHosts):
        self.es = Elasticsearch(elasticHosts)

    def index(self, timestamp, upSpeed, downSpeed):
        doc = {
            'timestamp': timestamp,
            'upSpeed': upSpeed,
            'downSpeed': downSpeed
        }

        self.es.index(index="speedtest", body=doc)
