# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest11937():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
