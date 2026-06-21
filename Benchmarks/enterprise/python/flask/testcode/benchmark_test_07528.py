# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest07528(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
