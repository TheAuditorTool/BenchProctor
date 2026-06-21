# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest36674():
    raw_body = request.get_data(as_text=True)
    data = to_text(raw_body)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
