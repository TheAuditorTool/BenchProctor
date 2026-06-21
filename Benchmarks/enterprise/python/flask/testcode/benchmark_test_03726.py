# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from app_runtime import db


def BenchmarkTest03726():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(db_value)
    return jsonify({"result": "success"})
