# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest34291():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
