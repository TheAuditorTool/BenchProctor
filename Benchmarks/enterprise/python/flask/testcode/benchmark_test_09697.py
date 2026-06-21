# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest09697():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    processed = data[:64]
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return jsonify({"result": "success"})
