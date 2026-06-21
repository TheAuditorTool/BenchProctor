# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest07082():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
