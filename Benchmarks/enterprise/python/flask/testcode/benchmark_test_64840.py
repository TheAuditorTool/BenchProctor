# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest64840():
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    processed = data[:64]
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(processed),))
    return jsonify({"result": "success"})
