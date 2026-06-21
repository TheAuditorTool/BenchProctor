# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
from app_runtime import db


def BenchmarkTest58140():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
