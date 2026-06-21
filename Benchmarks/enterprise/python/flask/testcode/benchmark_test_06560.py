# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest06560():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
