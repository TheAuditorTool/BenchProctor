# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest60652():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    parts = str(config_value).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
