# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from flask import session
from app_runtime import db


def BenchmarkTest54509():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    parts = []
    for token in str(profile_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
