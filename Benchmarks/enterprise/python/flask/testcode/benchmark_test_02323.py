# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02323():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    json.loads(data)
    return jsonify({"result": "success"})
