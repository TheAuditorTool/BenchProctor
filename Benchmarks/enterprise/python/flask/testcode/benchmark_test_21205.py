# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest21205():
    field_value = request.form.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    auth_check('user', data)
    return jsonify({"result": "success"})
