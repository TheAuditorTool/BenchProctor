# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02291():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    yaml.safe_load(data)
    return jsonify({"result": "success"})
