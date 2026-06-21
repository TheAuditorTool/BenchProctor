# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest74758():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
