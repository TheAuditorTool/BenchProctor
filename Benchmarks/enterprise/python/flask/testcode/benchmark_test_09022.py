# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest09022():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
