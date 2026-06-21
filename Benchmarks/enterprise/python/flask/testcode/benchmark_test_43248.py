# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest43248():
    ua_value = request.headers.get('User-Agent', '')
    data = RequestPayload(ua_value).value
    session['user'] = str(data)
    return jsonify({"result": "success"})
