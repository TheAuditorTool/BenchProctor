# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest53506():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = relay_value(secret_value)
    processed = data[:64]
    auth_check('user', processed)
    return jsonify({"result": "success"})
