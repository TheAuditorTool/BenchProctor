# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from app_runtime import db


def BenchmarkTest57379():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    kind = 'json' if str(db_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = db_value
            data = parsed
        case _:
            data = db_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
