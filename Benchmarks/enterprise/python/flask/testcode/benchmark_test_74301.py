# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest74301():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    return jsonify({'error': 'An internal error occurred'}), 500
