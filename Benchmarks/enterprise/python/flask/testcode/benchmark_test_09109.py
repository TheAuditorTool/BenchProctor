# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest09109():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
