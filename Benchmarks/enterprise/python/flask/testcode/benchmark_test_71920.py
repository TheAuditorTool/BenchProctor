# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest71920():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = relay_value(config_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
