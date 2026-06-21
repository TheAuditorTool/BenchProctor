# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest53698():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})
