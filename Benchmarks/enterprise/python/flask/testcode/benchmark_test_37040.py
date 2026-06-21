# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest37040():
    secret_value = 'config_secret_test_abc123'
    data = to_text(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
