# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest02162():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})
