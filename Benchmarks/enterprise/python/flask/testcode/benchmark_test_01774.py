# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest01774():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    divisor = int(str(db_value)) if str(db_value).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
