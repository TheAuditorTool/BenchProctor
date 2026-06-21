# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db, auth_check


def BenchmarkTest03585():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
