# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest21606():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
