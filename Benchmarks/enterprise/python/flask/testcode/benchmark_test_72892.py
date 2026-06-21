# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest72892():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return jsonify({'error': 'An internal error occurred'}), 500
