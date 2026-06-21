# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest69048():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
