# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest32107():
    auth_header = request.headers.get('Authorization', '')
    data = RequestPayload(auth_header).value
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
