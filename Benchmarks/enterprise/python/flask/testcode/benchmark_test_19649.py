# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest19649():
    secret_value = 'config_secret_test_abc123'
    auth_check('user', secret_value)
    return jsonify({"result": "success"})
