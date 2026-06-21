# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest64233():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
