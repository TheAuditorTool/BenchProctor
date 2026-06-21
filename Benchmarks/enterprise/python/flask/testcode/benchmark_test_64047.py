# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest64047():
    field_value = request.form.get('field', '')
    data = ensure_str(field_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
