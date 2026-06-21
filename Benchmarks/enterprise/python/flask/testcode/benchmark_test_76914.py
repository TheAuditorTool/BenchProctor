# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest76914():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = RequestPayload(dotenv_value).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
