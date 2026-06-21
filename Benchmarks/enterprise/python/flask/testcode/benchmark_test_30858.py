# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest30858():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    session['data'] = str(data)
    return jsonify({"result": "success"})
