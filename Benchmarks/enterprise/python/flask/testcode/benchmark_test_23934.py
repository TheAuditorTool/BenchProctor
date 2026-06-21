# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def BenchmarkTest23934():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
