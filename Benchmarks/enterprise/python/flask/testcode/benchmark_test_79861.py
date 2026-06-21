# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest79861():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(db_value),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
