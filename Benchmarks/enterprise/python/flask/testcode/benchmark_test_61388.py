# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest61388():
    secret_value = 'config_secret_test_abc123'
    data = str(secret_value).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
