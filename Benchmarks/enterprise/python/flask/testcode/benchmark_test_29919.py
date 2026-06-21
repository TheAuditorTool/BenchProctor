# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest29919():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
