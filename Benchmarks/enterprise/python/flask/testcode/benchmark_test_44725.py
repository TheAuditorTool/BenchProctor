# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify


def BenchmarkTest44725():
    secret_value = 'config_secret_test_abc123'
    data = f'{secret_value:.200s}'
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return jsonify({"result": "success"})
