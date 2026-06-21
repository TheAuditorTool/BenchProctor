# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest60212():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = str(config_value).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
