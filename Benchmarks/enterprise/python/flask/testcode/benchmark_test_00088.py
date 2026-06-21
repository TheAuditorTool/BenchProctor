# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest00088():
    secret_value = 'config_secret_test_abc123'
    if secret_value:
        data = secret_value
    else:
        data = ''
    auth_check('user', data)
    return jsonify({"result": "success"})
