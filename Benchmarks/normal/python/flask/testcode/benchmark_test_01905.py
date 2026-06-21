# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest01905():
    referer_value = request.headers.get('Referer', '')
    data = ensure_str(referer_value)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
