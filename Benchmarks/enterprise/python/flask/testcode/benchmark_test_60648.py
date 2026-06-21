# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest60648():
    upload_name = request.files['upload'].filename
    data = RequestPayload(upload_name).value
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
