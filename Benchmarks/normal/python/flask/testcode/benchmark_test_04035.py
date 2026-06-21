# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest04035(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
