# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest20301():
    secret_value = 'config_secret_test_abc123'
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    auth_check('user', data)
    return jsonify({"result": "success"})
