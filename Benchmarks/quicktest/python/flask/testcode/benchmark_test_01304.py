# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest01304(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    json.loads(data)
    return jsonify({"result": "success"})
