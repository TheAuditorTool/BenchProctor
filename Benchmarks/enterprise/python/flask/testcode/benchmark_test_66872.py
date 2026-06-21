# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest66872():
    secret_value = 'config_secret_test_abc123'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
