# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest60715():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = f'{secret_value:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
