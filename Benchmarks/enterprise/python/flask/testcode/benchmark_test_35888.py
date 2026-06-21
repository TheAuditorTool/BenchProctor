# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest35888():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
