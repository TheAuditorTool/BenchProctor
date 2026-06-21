# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
import json
from app_runtime import db, auth_check


def BenchmarkTest68047():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
