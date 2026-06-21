# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest19728():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if not auth_check(str(forwarded_ip), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
