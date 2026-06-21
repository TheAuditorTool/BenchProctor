# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify


def BenchmarkTest12486():
    secret_value = 'config_secret_test_abc123'
    data = secret_value if secret_value else 'default'
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return jsonify({"result": "success"})
