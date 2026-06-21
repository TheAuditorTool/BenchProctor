# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest13197():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = ' '.join(str(secret_value).split())
    auth_check('user', data)
    return jsonify({"result": "success"})
