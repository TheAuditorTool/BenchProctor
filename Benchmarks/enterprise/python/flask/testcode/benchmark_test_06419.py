# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify


def BenchmarkTest06419():
    secret_value = 'config_secret_test_abc123'
    data, _sep, _rest = str(secret_value).partition('\x00')
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return jsonify({"result": "success"})
