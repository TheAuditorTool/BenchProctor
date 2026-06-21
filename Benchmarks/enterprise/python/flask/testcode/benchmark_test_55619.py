# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest55619():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return jsonify({"result": "success"})
