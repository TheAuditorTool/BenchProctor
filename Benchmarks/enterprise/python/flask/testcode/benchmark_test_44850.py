# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest44850():
    upload_name = request.files['upload'].filename
    data = RequestPayload(upload_name).value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
