# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest20166():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = (lambda v: v.strip())(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
