# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest72574():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(config_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
