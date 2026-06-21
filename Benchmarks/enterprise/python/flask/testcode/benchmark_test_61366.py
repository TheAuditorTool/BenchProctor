# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest61366():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    int(str(data))
    return jsonify({"result": "success"})
