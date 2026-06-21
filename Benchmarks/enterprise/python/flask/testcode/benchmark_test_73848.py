# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def BenchmarkTest73848():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
