# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import session
from flask import jsonify
import os


def BenchmarkTest80768():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    def normalize(value):
        return value.strip()
    data = normalize(dotenv_value)
    session.clear()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
