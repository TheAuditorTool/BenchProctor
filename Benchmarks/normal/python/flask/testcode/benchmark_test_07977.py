# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest07977():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
