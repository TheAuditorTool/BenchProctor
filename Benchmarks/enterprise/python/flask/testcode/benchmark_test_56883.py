# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest56883():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
