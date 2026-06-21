# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest47969():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
