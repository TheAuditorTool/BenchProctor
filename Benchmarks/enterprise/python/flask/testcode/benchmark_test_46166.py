# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest46166():
    raw_body = request.get_data(as_text=True)
    data = to_text(raw_body)
    auth_check('user', data)
    return jsonify({"result": "success"})
