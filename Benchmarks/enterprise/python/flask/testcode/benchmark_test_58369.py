# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest58369():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
