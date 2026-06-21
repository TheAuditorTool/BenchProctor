# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest27976():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    auth_check('user', secret_value)
    return jsonify({"result": "success"})
