# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest61586():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
