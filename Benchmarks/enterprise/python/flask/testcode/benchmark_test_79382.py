# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest79382():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    auth_check('user', data)
    return jsonify({"result": "success"})
