# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from flask import session
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest40497():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = handle(dotenv_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
