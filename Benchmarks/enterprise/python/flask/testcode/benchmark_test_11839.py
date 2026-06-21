# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest11839(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})
