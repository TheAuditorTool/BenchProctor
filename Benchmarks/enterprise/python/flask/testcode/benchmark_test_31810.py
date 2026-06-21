# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest31810():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
