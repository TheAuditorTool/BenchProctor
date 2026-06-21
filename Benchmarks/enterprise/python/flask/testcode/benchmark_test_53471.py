# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest53471():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
