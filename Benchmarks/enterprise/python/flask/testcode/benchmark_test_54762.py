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

def BenchmarkTest54762():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
