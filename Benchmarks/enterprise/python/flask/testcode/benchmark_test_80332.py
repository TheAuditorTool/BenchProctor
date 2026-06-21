# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest80332():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    if secret_value:
        data = secret_value
    else:
        data = ''
    auth_check('user', data)
    return jsonify({"result": "success"})
