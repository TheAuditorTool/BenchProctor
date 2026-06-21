# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest01500():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
