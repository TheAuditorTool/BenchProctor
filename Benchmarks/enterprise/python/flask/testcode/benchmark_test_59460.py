# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest59460(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
