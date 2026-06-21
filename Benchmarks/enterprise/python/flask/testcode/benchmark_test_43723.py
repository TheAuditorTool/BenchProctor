# SPDX-License-Identifier: Apache-2.0
import base64
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def BenchmarkTest43723():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
