# SPDX-License-Identifier: Apache-2.0
import secrets
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest08925():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
