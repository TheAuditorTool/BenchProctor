# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest34164():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
