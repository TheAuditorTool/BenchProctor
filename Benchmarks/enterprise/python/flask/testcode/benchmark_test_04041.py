# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def BenchmarkTest04041():
    env_value = os.environ.get('USER_INPUT', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
