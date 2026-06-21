# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest80445():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
