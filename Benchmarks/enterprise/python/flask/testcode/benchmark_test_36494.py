# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
from app_runtime import db


def BenchmarkTest36494():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
