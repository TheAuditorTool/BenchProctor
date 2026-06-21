# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest20623():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = coalesce_blank(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
