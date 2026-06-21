# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from app_runtime import db


def BenchmarkTest02175():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    session['user'] = str(data)
    return jsonify({"result": "success"})
