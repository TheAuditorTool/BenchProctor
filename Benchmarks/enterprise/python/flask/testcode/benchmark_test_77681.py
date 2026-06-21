# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json


def BenchmarkTest77681():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = json.loads(config_value).get('value', config_value)
    except (json.JSONDecodeError, AttributeError):
        data = config_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
