# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest17654():
    ua_value = request.headers.get('User-Agent', '')
    data = RequestPayload(ua_value).value
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
