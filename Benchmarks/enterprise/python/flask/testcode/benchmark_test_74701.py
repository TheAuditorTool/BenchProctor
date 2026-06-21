# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest74701():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = str(ast.literal_eval(profile_value))
    except (ValueError, SyntaxError):
        data = profile_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
