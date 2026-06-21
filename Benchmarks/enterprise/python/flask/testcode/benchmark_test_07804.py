# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest07804():
    referer_value = request.headers.get('Referer', '')
    if referer_value != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    if not auth_check(session.get('user', ''), str(referer_value)):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
