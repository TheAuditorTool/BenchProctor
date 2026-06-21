# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def BenchmarkTest28888():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
