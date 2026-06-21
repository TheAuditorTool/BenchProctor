# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest33457():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    auth_check('user', data)
    return jsonify({"result": "success"})
