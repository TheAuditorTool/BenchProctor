# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def BenchmarkTest51068():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if not auth_check(str(db_value), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
