# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest53491():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
