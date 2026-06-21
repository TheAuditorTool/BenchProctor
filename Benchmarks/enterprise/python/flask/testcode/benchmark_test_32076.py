# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest32076():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = str(ast.literal_eval(profile_value))
    except (ValueError, SyntaxError):
        data = profile_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
