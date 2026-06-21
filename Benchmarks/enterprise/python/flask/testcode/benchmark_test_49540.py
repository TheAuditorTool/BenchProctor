# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest49540():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
