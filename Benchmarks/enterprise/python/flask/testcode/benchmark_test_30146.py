# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from flask import current_app
from datetime import timedelta


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest30146():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
