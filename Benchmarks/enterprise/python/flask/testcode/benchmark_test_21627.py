# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest21627():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
