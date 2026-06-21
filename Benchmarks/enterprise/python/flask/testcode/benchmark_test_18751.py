# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from flask import session
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest18751():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = coalesce_blank(dotenv_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
