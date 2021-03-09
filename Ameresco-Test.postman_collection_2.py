#!/usr/bin/env python
"""

"""

import logging
import argparse
import configparser
import requests
import json
import datetime

logger = logging.getLogger('ian testing')
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
logger.addHandler(console)

key = '85E48037-25F4-4D29-8D36-2C47BA56BFB7.01'
base_url = 'https://portal.solarpark-online.com/'


def get_source_id(api_key, site_ids=[], mlocs=[]):
    logger.info('getting source ids using mlocs')

    header = {
        'Api-Key': api_key,
        'Content-Type': 'application/json',
    }

    body = {
        'site_ids': ','.join(site_ids),
        'segment_apcodes': 'Site',
        'mlocs': ','.join(mlocs),
        'stngs': '',
        'svars': ''
    }

    r = requests.post(base_url + 'ifms/segments/sites/query', headers=header, json=body)

    logger.info(r.status_code)
    logger.debug(r.headers)
    logger.debug(r.content)

    data = r.json()
    # logger.debug(data)

    ids = []
    for site in data:
        for mloc in site['mlocs']:
            ids.append(mloc['msrc']['id'])

    return ids


def get_batch_data(api_key, source_ids, start_date, end_date):

    logger.info('getting multiple time series data for multiple data points')
    header = {
        'Api-Key': api_key,
        'Content-Type': 'application/json',
    }

    params = {
        'start_date': start_date,
        'end_date': end_date
    }

    body = '[' + ', '.join('"{0}"'.format(w) for w in source_ids) + ']'

    r = requests.post(base_url + 'ifms/sources/values', headers=header, params=params, data=body)
    logger.debug(r.status_code)
    logger.debug(r.headers)
    logger.debug(r.content)

    return r.json()


if __name__ == "__main__":
    siteids = [
        '06e153c2-e109-11e8-afaf-42010afa015a',
        '0ca806f4-e369-11e8-b000-42010afa015a',
        '16ba102c-de8e-11e8-9b61-42010afa015a',
        '3032a45e-de81-11e8-920c-42010afa015a',
        '3085543c-b042-11e8-848a-42010afa015a'
    ]

    mlocs = [
        'ArrayOutputPower',
        'ActivePowerToUtility',
        'AverageIrradiance',
        'AverageAmbientAirTemperature',
        'AverageModuleTemperature'
    ]

    source_ids = get_source_id(key, siteids, mlocs)
    time_data = get_batch_data(key, source_ids, '20190901T000000Z', '20190904T234500Z')
