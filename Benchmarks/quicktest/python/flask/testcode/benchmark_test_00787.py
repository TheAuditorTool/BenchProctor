# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest00787():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
