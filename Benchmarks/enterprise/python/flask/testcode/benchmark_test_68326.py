# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest68326():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
