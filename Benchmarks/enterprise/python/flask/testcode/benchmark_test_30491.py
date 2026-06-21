# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import os


def BenchmarkTest30491():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = (lambda v: v.strip())(dotenv_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
