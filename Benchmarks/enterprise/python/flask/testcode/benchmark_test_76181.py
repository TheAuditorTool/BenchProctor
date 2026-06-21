# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest76181():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
