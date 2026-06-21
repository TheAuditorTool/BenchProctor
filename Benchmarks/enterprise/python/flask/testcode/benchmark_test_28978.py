# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest28978():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
