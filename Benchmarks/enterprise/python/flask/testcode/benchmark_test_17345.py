# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest17345():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = default_blank(config_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
