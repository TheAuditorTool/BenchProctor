# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest16966():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
