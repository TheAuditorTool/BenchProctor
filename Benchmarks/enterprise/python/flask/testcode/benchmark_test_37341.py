# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest37341():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(db_value), store_cred)
    return jsonify({"result": "success"})
