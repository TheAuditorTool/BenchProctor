# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest64052():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    requests.post('http://api.prod.internal/data', data=str(config_value))
    return jsonify({"result": "success"})
