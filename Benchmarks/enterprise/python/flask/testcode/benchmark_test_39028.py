# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest39028():
    secret_value = 'config_secret_test_abc123'
    data, _sep, _rest = str(secret_value).partition('\x00')
    auth_check('user', data)
    return jsonify({"result": "success"})
