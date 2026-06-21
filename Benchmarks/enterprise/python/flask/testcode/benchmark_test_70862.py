# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest70862():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    if config_value:
        data = config_value
    else:
        data = ''
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
