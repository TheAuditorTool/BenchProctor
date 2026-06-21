# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest36017():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    if secret_value:
        data = secret_value
    else:
        data = ''
    auth_check('user', data)
    return jsonify({"result": "success"})
