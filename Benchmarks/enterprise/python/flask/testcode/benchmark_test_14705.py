# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest14705():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
