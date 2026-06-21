# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import session
from flask import jsonify
from app_runtime import db


def BenchmarkTest76178():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    prefix = ''
    data = prefix + str(profile_value)
    session.clear()
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
