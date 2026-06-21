# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest79391():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
