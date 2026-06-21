# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest39325():
    referer_value = request.headers.get('Referer', '')
    data = RequestPayload(referer_value).value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
