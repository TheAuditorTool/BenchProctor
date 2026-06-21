# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest44497():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = str(config_value).replace('\x00', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
