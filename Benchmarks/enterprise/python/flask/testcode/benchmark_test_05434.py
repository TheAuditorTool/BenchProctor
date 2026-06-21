# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest05434():
    field_value = request.form.get('field', '')
    auth_check('user', field_value)
    return jsonify({"result": "success"})
