# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest52534():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
