# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from flask import session
from app_runtime import db


def BenchmarkTest31414():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
