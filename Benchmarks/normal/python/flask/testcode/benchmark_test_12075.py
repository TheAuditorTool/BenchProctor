# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest12075():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
