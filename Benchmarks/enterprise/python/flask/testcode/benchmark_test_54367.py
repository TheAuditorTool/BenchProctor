# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db, auth_check


request_state: dict[str, str] = {}

def BenchmarkTest54367():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
