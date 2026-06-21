# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest74081():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        result = int(str(db_value))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
