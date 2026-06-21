# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest47534():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
