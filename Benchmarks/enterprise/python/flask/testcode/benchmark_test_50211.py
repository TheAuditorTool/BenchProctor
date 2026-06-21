# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest50211():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
