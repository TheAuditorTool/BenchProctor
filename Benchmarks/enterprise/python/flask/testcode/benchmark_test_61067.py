# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest61067():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
