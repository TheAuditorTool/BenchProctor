# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest57705():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
