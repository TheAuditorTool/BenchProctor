# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest03205():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = str(db_value).replace('\x00', '')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
