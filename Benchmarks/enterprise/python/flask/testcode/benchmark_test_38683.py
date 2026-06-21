# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest38683():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
