# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest09104():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return jsonify({'error': str(db_value), 'stack': repr(locals())}), 500
