# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest51819():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
