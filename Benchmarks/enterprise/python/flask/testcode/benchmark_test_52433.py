# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest52433(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
