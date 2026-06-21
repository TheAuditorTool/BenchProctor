# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest73894():
    secret_value = 'config_secret_test_abc123'
    data = secret_value if secret_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})
