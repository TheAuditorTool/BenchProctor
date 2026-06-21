# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from flask import session
from app_runtime import db, auth_check


def BenchmarkTest75393():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
