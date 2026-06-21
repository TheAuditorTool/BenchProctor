# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest69667():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
