# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest16239():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    requests.get(str(data))
    return jsonify({"result": "success"})
