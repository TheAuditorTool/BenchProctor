# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest18754():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    json.loads(data)
    return jsonify({"result": "success"})
