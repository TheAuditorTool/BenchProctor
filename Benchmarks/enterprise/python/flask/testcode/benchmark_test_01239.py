# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify
from flask import current_app
from datetime import timedelta


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest01239():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
