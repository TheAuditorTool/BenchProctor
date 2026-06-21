# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from app_runtime import db


def BenchmarkTest43899():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session['data'] = str(data)
    return jsonify({"result": "success"})
