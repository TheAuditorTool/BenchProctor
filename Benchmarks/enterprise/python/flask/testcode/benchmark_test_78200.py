# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest78200():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
