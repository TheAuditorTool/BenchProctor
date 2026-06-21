# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest65545():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
