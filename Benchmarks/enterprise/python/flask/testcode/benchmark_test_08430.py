# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from flask import session
from app_runtime import db


def BenchmarkTest08430():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(profile_value)
    data = collected
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
