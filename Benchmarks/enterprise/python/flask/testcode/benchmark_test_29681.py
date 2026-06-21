# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest29681():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
