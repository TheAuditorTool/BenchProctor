# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest48971():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if data != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
