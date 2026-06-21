# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02914():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    os.remove(str(data))
    return jsonify({"result": "success"})
