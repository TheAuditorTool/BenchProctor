# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest71390():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = secret_value if secret_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})
