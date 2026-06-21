# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest66563():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
