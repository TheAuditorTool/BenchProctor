# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03532():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
