# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest66507():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    session['data'] = str(data)
    return jsonify({"result": "success"})
