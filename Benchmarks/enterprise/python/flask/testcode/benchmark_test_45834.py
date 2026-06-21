# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest45834():
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
