# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def BenchmarkTest04923():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if not auth_check(session.get('user', ''), str(db_value)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
