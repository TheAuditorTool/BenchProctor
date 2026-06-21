# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def BenchmarkTest45950():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    prefix = ''
    data = prefix + str(db_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
