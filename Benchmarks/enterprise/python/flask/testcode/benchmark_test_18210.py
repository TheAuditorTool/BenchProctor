# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest18210():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    return jsonify({'error': 'An internal error occurred'}), 500
