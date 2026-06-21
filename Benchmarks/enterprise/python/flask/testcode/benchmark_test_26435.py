# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest26435():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
