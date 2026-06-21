# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest49342(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
