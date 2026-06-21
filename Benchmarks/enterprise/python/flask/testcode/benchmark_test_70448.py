# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest70448(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    os.remove(str(data))
    return jsonify({"result": "success"})
