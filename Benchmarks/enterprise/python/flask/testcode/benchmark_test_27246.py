# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest27246():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = RequestPayload(json_value).value
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
