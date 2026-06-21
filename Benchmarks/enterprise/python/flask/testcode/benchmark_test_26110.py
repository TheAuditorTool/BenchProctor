# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest26110():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    auth_check('user', secret_value)
    return jsonify({"result": "success"})
