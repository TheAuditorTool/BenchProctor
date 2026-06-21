# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest46713():
    secret_value = 'config_secret_test_abc123'
    data = f'{secret_value:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
