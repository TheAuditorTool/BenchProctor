# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest24116():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
