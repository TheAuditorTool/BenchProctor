# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest30361():
    secret_value = 'config_secret_test_abc123'
    data = RequestPayload(secret_value).value
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
