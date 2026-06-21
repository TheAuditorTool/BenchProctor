# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest37404():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
