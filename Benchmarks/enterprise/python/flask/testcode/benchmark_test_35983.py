# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import jsonify


def BenchmarkTest35983():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
