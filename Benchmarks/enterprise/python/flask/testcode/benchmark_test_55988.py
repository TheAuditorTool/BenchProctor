# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest55988():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = RequestPayload(json_value).value
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
