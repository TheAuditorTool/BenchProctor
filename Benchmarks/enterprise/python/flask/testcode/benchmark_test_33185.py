# SPDX-License-Identifier: Apache-2.0
from flask import session
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest33185():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
