# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest25387():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '{}'.format(db_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
