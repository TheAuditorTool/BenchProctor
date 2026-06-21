# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import json


def BenchmarkTest61348():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = json.loads(config_value).get('value', config_value)
    except (json.JSONDecodeError, AttributeError):
        data = config_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
