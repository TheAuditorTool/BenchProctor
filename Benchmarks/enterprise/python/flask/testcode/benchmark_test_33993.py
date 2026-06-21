# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import db, auth_check


def BenchmarkTest33993():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    auth_check('user', data)
    return jsonify({"result": "success"})
