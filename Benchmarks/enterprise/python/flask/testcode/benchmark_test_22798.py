# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest22798():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return jsonify({"result": "success"})
