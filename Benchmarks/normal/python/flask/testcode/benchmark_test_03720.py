# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03720():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
