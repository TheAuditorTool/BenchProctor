# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import jsonify
from app_runtime import db


def BenchmarkTest10585():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(db_value), max_age=86400)
    return resp
