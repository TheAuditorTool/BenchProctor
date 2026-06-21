# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest45097():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = str(secret_value).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
