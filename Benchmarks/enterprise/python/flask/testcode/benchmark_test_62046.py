# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify


def BenchmarkTest62046():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = str(secret_value).replace('\x00', '')
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return jsonify({"result": "success"})
