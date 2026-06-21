# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest39159():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
