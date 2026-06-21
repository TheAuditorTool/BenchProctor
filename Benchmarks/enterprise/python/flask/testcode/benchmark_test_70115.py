# SPDX-License-Identifier: Apache-2.0
import base64
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def BenchmarkTest70115():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
