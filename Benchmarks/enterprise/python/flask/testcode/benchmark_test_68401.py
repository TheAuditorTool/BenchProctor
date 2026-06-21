# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest68401():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
