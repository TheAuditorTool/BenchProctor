# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def BenchmarkTest59588():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(db_value)):
        return jsonify({'error': 'invalid input'}), 400
    processed = db_value
    eval(str(processed))
    return jsonify({"result": "success"})
