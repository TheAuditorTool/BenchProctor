# SPDX-License-Identifier: Apache-2.0
import threading
from flask import jsonify
from app_runtime import db


def BenchmarkTest80876():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
