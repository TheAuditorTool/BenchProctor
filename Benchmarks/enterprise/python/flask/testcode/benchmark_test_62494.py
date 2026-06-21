# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest62494(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
