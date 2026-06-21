# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest75857():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    db.execute('SELECT * FROM users WHERE id = ?', (db_value,))
    return jsonify({"result": "success"})
