# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest41802():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = RequestPayload(config_value).value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
