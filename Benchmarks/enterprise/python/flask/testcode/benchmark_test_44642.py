# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest44642():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
