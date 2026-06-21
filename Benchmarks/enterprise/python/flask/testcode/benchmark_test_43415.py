# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify


def BenchmarkTest43415():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return jsonify({"result": "success"})
