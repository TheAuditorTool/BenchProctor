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

def BenchmarkTest32924():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
