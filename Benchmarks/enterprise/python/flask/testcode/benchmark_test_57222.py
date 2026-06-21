# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest57222():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = RequestPayload(forwarded_ip).value
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
