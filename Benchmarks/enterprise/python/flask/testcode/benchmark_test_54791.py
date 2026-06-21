# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest54791():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = config_value if config_value else 'default'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
