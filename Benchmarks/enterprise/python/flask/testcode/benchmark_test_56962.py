# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest56962():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
