# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest05697():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    auth_check('user', secret_value)
    return jsonify({"result": "success"})
