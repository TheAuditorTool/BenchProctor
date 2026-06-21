# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib
import sys


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest81137():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
