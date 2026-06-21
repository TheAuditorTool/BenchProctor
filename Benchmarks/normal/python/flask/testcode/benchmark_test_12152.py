# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest12152():
    origin_value = request.headers.get('Origin', '')
    data = to_text(origin_value)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
