# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest53742():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})
