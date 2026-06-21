# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import json


def BenchmarkTest42655():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    try:
        data = json.loads(prop_value).get('value', prop_value)
    except (json.JSONDecodeError, AttributeError):
        data = prop_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
