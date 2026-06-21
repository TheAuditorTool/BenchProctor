# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest14413():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    prefix = ''
    data = prefix + str(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
