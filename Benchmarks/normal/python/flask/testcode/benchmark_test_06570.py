# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify


def BenchmarkTest06570():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = secret_value if secret_value else 'default'
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return jsonify({"result": "success"})
