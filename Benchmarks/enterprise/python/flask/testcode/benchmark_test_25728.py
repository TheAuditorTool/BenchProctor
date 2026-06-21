# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest25728():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
