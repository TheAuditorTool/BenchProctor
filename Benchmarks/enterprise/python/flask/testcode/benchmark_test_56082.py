# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest56082():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(config_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
