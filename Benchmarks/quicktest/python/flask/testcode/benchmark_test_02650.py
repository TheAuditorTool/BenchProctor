# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02650():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
