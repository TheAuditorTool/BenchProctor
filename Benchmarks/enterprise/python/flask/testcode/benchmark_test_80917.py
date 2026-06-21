# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest80917():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = secret_value if secret_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})
