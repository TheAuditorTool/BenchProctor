# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest08352():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(db_value),))
    return jsonify({'record': str(record)}), 200
