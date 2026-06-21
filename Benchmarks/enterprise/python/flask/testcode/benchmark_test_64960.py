# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest64960(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
