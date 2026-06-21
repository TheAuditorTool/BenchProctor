# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest36269():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
