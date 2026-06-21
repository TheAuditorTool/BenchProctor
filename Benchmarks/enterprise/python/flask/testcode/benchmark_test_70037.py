# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest70037():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data, _sep, _rest = str(secret_value).partition('\x00')
    auth_check('user', data)
    return jsonify({"result": "success"})
