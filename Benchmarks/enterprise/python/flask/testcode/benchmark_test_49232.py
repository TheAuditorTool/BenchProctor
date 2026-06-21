# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db


def BenchmarkTest49232():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
