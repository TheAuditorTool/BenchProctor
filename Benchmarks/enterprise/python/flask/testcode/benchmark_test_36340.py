# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest36340():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = relay_value(yaml_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
