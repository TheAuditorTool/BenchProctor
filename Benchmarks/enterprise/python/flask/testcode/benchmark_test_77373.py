# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest77373():
    secret_value = 'config_secret_test_abc123'
    data = (lambda v: v.strip())(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
