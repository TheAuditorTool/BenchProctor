# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest22100():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    prefix = ''
    data = prefix + str(config_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
