# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest54607(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    json.loads(data)
    return jsonify({"result": "success"})
