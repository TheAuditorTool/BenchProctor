# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest39944():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if not auth_check(session.get('user', ''), str(forwarded_ip)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
