# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest07248():
    host_value = request.headers.get('Host', '')
    data = normalise_input(host_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
