# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest67093():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    db.execute('SELECT * FROM users WHERE id = ' + str(db_value))
    return jsonify({"result": "success"})
