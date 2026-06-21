# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest68815():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
