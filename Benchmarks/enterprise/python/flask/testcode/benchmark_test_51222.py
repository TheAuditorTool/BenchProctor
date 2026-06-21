# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest51222():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = normalise_input(secret_value)
    processed = data[:64]
    auth_check('user', processed)
    return jsonify({"result": "success"})
