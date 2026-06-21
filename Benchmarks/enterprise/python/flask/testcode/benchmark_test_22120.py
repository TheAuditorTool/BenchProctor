# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def BenchmarkTest22120():
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
