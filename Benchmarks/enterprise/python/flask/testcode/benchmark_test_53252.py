# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def BenchmarkTest53252():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
