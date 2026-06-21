# SPDX-License-Identifier: Apache-2.0
from flask import session
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest18125():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
