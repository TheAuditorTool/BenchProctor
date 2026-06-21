# SPDX-License-Identifier: Apache-2.0
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest26934():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
