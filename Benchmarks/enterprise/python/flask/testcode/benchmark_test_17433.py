# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest17433():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    auth_check('user', data)
    return jsonify({"result": "success"})
