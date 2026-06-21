# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest05734():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
