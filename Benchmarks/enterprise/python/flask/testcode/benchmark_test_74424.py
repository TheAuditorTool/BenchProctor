# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest74424():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = handle(secret_value)
    processed = data[:64]
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return jsonify({"result": "success"})
