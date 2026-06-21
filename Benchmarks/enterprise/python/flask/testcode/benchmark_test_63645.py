# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest63645():
    origin_value = request.headers.get('Origin', '')
    data = ensure_str(origin_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
