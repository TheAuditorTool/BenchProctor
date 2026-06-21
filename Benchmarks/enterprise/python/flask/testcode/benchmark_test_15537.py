# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest15537():
    referer_value = request.headers.get('Referer', '')
    data = RequestPayload(referer_value).value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
