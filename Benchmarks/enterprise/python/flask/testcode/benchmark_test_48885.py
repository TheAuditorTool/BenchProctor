# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest48885():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = ensure_str(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
