# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest04869():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ensure_str(db_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
