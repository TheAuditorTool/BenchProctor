# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest78778():
    xml_value = request.get_data(as_text=True)
    data = RequestPayload(xml_value).value
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
