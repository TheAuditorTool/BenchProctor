# SPDX-License-Identifier: Apache-2.0
import logging
import json
from flask import jsonify


def BenchmarkTest41116():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
