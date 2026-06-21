# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def BenchmarkTest02715():
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
