# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest27243():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    eval(str(data))
    return jsonify({"result": "success"})
