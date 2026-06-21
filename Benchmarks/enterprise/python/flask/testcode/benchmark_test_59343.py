# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest59343():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
