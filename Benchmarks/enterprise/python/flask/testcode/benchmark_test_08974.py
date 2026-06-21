# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest08974():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
