# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02774():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
