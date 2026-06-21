# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest52086():
    secret_value = 'config_secret_test_abc123'
    data = normalise_input(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
