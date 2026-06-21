# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest47956():
    upload_name = request.files['upload'].filename
    if upload_name != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    if not auth_check(session.get('user', ''), str(upload_name)):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
