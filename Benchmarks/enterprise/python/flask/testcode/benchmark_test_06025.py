# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest06025():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(db_value))
    return jsonify({'lookup': arr[idx]}), 200
