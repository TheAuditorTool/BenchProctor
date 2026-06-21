# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest12185():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
