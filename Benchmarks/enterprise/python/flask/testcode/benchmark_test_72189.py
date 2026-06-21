# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from app_runtime import db


def BenchmarkTest72189():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(profile_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
