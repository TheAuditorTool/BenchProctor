# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest22043():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    parts = str(config_value).split(',')
    data = ','.join(parts)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
