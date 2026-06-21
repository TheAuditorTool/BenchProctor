# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest07721():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
