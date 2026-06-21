# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest68697():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '%s' % str(config_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
