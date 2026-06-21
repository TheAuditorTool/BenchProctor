# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest53656():
    xml_value = request.get_data(as_text=True)
    data = RequestPayload(xml_value).value
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
