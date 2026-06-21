# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import jsonify


def BenchmarkTest43525():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = json.loads(config_value).get('value', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
